/************************************************************************************
 * A basic IR system using Lucene                                                   *
 *                                                                                  *
 * including:                                                                       *
 *     - index building                                                             *
 *     - query processing                                                           *
 *     - result printing                                                            *
 *                                                                                  *
 * author: yannick . parmentier @ loria . fr                                        *
 *                                                                                  *
 * Usage:                                                                           *
 *    javac -cp .:lucene-core-7.2.1.jar:lucene-queryparser-7.2.1 BasicIRsystem.java *                      
 *    java -cp .:lucene-core-7.2.1.jar:lucene-queryparser-7.2.1 BasicIRsystem\      *
 *                 collection_path index_path                                       *
 *                                                                                  *
 *                                                                                  *
 *                                                                    2018/02/14    *
 *                                                                                  *
 ************************************************************************************/

import java.io.*;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.*;
import org.apache.lucene.analysis.*;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.*;
import org.apache.lucene.search.*;
import org.apache.lucene.store.*;
import org.apache.lucene.document.*;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.queryparser.classic.ParseException;

/**
 * BasicIRsystem class
 */
public class BasicIRsystem {

    public static String indexPlace;

    public static void createIndex(String path) throws Exception {
	BasicIRsystem.indexPlace = path;
	Directory directory = FSDirectory.open(Paths.get(indexPlace));

	IndexWriterConfig config = new IndexWriterConfig(new StandardAnalyzer());
	IndexWriter  indexWriter = new IndexWriter(directory, config);
	File                 dir = new File(path);
	String[]           files = dir.list();

	for(int i = 0 ; i < files.length ; i++) {
		if ((path + "\\" + files[i]).matches("(.*).txt")){
			Document d = indexDoc(path + "\\" + files[i]);
			indexWriter.addDocument(d);
		}
	}
		System.out.println("mmh");
		indexWriter.close();
		System.out.println("ok");

	}
    
    public static Document indexDoc(String file) throws Exception {
	Document d = new Document();
	FileInputStream is = new FileInputStream(file);
	d.add(new Field("path", file, TextField.TYPE_STORED));	
	d.add(new Field("content", new String(Files.readAllBytes(Paths.get(file))), TextField.TYPE_STORED));
	return d;
    }

    public static Document[] processQuery(String queryString) throws IOException, ParseException {
	Analyzer       analyzer = new StandardAnalyzer();
	Directory     directory = FSDirectory.open(Paths.get(indexPlace));
	DirectoryReader ireader = DirectoryReader.open(directory);
	IndexSearcher       is  = new IndexSearcher(ireader);
	QueryParser      parser = new QueryParser("content", analyzer);
	Query             query = parser.parse(queryString);
	ScoreDoc[]         hits = is.search(query, 1000).scoreDocs; //top 1000 docs
	System.out.println(hits.length + " result(s) found");
	Document[]         docs = new Document[hits.length];
	for(int i = 0 ; i < hits.length ; i++) {
	    Document doc = is.doc(hits[i].doc);
	    docs[i] = doc;
	}
	return docs;
    }
    
    public static void main(String [] args) {
	try {
	    String collectionPath = "D:\\collection";
		indexPlace = "D:\\index";
		createIndex(collectionPath);
	    String q = " ";
	    while (true) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Please enter your query: (-1 to quit)");
		q = sc.next();
		if (q.equals("-1")) {break;} //to quit

		Document[] results = processQuery(q);
		for(Document d : results) {
		    System.out.println(d.get("path"));
		}
		
	    } 
	    
	} catch (Exception e) {
	    System.err.println("oops");
	    System.err.println(e.toString());
	}   
    }
}
