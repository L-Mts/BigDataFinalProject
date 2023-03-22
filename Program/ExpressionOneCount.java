import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class ExpressionOneCount {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
        //get next token + replace all non-letter to a "."
        String str = itr.nextToken().replaceAll("[^a-zA-Z]",".");
        str.toLowerCase();
        //check if str[7] is a "." (character at the end of "climate")
        if(str.length()>7) {
          if(str.charAt(7) == '.') {
            //split before the "."
            String[] separated = str.split(".");
            if(separated[0].equals("climate")) {
              if(itr.hasMoreTokens()){
                  String str2 = itr.nextToken().replaceAll("[^a-zA-Z]",".");
                  str2.toLowerCase();
                  if(str2.length()>6) {
                    if(str2.charAt(6) == '.') {
                      String[] separated2 = str.split(".");
                      if(separated2[0].equals("change")) {
                          String strfinal = separated[0]+" "+separated2[0]+",";
                          word.set(strfinal);
                          context.write(word,one);
                      }
                    }
                  }
                  if (str2.equals("change")){
                    String strfinal = separated[0]+" "+str2+",";
                    word.set(strfinal);
                    context.write(word,one);
                  }
              }
            }
          }
        }
        if (str.equals("climate")) {
          if(itr.hasMoreTokens()){
            String str2 = itr.nextToken().replaceAll("[^a-zA-Z]",".");
            str2.toLowerCase();
            if(str2.length()>6) {
              if(str2.charAt(6) == '.') {
                String[] separated2 = str.split(".");
                if(separated2[0].equals("change")) {
                    String strfinal = str+" "+separated2[0]+",";
                    word.set(strfinal);
                    context.write(word,one);
                }
              }
            }
            if (str2.equals("change")){
              String strfinal = str+" "+str2+",";
              word.set(strfinal);
              context.write(word,one);
            }
        }

        }
        
        /*
        if(str.equals("global")) {
            if(itr.hasMoreTokens()){
                String str2 = itr.nextToken().replaceAll("[^a-zA-Z]","");
                str2.toLowerCase();
                if(str2.equals("warming")) {
                    String strfinal = str+" "+str2+",";
                    word.set(strfinal);
                    context.write(word,one);
                }
            }
        }
        if(str.equals("natural")) {
            if(itr.hasMoreTokens()){
                String str2 = itr.nextToken().replaceAll("[^a-zA-Z]","");
                str2.toLowerCase();
                if(str2.equals("disaster")) {
                    String strfinal = str+" "+str2+",";
                    word.set(strfinal);
                    context.write(word,one);
                }
            }
        }
        */
      }
    }
  }

  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(ExpressionOneCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}