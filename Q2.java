package query2;

import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.lang.*;
import java.util.*; 

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapOutputCollector.Context;
import org.apache.hadoop.mapred.TextOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;

public class Q2{

  public static class Mapper1 extends Mapper<Text, Text, Text, IntWritable>
  {

	private Text newKey;
	private IntWritable newVal;

    public void map(Text key, Text value, Context context) throws IOException, InterruptedException 
    {
		Configuration conf = context.getConfiguration();
		String grouping = conf.get("grouping");
		int funcCol = Integer.parseInt(conf.get("funcCol"));
		String nk = "";
		int nv; 
		
		ArrayList<String> fields= new ArrayList<>();
		
		StringTokenizer st = new StringTokenizer(value.toString(),",");
		
		while(st.hasMoreTokens())
		{
			fields.add(st.nextToken());
		}
		
		if(grouping.charAt(0) == '1')
		{
			nk += key.toString();
		}
		
		for(int i = 1;i < grouping.length();i++)
		{
			if(grouping.charAt(i)== '1')
			{
				if(nk != "")
					nk += "\t";
				nk += fields.get(i-1);
			}
		}
		
		if(funcCol == 0)
			nv = Integer.parseInt(key.toString());
		else
			nv = Integer.parseInt(fields.get(funcCol - 1));
		
		newKey = new Text(nk);
		newVal = new IntWritable(nv);
		
		context.write(newKey, newVal);
    }
   
  }

  public static class Reducer1 extends Reducer<Text,IntWritable,Text,IntWritable> {
	private IntWritable result;
	
	public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException 
	{
		Configuration conf = context.getConfiguration();
		int func = Integer.parseInt(conf.get("func"));
		int X = Integer.parseInt(conf.get("X"));
		int v = 0;
		
		switch(func)
		{
			case 0:
				v = 0;
				for(IntWritable val : values){
					v += 1;
				}
				break;
			
			case 1:
				v = Integer.MIN_VALUE;
				for(IntWritable val : values){
					v = Math.max(val.get(), v);
				}
				break;
				
			case 2:
				v = Integer.MAX_VALUE;
				for(IntWritable val : values){
					v = Math.min(v, val.get());
				}
				break;
			
			case 3:
				v = 0;
				for(IntWritable val : values){
					v += val.get();
				}
				break;
		}
		
		if(v > X)
		{
			result = new IntWritable(v);
			context.write(key,result);
		}
	}
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    conf.set("func",args[2]); // 0 -> Count, 1-> MAX, 2->MIN, 3-> SUM
    conf.set("X",args[3]);
    conf.set("grouping",args[4]);
    conf.set("funcCol",args[5]);
    conf.set("mapreduce.input.keyvaluelinerecordreader.key.value.separator", ",");
    
    Job job = Job.getInstance(conf, "query 2");
    job.setJarByClass(Q2.class);
    
    job.setMapperClass(Mapper1.class);
    job.setCombinerClass(Reducer1.class);
    job.setReducerClass(Reducer1.class);
    
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    
    job.setInputFormatClass(KeyValueTextInputFormat.class);    
    KeyValueTextInputFormat.addInputPath(job, new Path(args[0]));
    
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}