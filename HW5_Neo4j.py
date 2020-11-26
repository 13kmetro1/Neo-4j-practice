import sys


#TODO: Write your username and answer to each query as a string in the return statements 
# in the functions below. Do not change the function names. 

# Write your queries using multi-line strings and use proper indentation to increase readability

#Your result should have the attributes in the same order as appeared in the sample answers. 

#Make sure to test that python prints out the strings correctly.

#usage: python hw5.py

def username():
	return "Kmetro"
    
def query5():
    return """
            MATCH (author:Author)-[:WRITES]->(article:Article)-[context:IN]->(issue)-[:OF]->(journal)
RETURN author.name, article.title 
           """ 

def query6():
    return """
            MATCH (author:Author)-[:WRITES]->(article:Article)-[context:IN]->(issue)-[:OF]->(journal)
RETURN author.name , article.title as paper_or_chapter, labels(article)as publicationType
UNION MATCH (author:Author)-[:WRITES]->(chapter:Chapter)-[context:IN]->(book)<-[:EDITS]-(editor:Author), (book)<-[:PUBLISHED_BY]-(pub:Publisher)
RETURN author.name ,chapter.title as paper_or_chapter, labels(chapter)as publicationType
           """ 

def query7():
    return """
            MATCH (author:Author)-[:WRITES]->(article:Article)-[context:IN]->(issue)-[:OF]->(journal)
RETURN author.name , article.title as paper_or_chapter, labels(article)as publicationType
UNION MATCH (author:Author)-[:WRITES]->(chapter:Chapter)-[context:IN]->(book)<-[:EDITS]-(editor:Author), (book)<-[:PUBLISHED_BY]-(pub:Publisher)
RETURN author.name ,chapter.title as paper_or_chapter, labels(chapter)as publicationType
Union match (author:Author)-[:EDITS]->(book:Book)
RETURN author.name , book.title as paper_or_chapter, labels(book)as publicationType
           """ 


def query8():
    return """
            MATCH (author:Author)-[:WRITES]->(article:Article)-[context:IN]->(issue)-[:OF]->(journal)
RETURN author.name , count(*) as publication_count
UNION MATCH (author:Author)-[:WRITES]->(chapter:Chapter)-[context:IN]->(book)<-[:EDITS]-(editor:Author), (book)<-[:PUBLISHED_BY]-(pub:Publisher)
RETURN author.name ,count(*)as publication_count
Union match (author:Author)-[:EDITS]->(book:Book)
RETURN author.name , count(*)as publication_count
           """ 


def query9():
    return """
            MATCH (author:Author)-[:WRITES]->(a:Article)-[context:IN]->(issue)-[:OF]->(journal)
where context.pp[1] - context.pp[0]+ 1 < 10
RETURN a.title, context.pp[1] - context.pp[0]+ 1 as numberOfPages
           """ 


def query10():
    return """
           MATCH (a1:Author)-[:WRITES]->(p1:Article)-[:CITES]->(p2)<-[:WRITES]-(a1:Author)
RETURN a1.name, p1.title, p2.title
           """ 


def query11():
    return """
            match p=()-[:CITES]->(publication)
with publication,count(publication) as pie
where pie >1
RETURN publication.title, pie as publication_count
           """ 


def query12():
    return """
            match p=()-[:CITES]->(article),(author:Author)-[:WRITES]->(article)-[context:IN]->(issue)-[:OF]->(journal)
with journal, article,author, count(article) as pie
where pie > 1
RETURN journal.title, article.title,pie as citations_count,author.name
           """ 


def query13():
    return """
            match (a1:Article)-[:IN]->(i1)-[:OF]->(journal)<-[:OF]-(i2)<-[:IN]-(a2:Article)
where (a1)-[:CITES]->(a2)
RETURN a1.title,  i1.issue, a2.title, i2.issue
           """ 


#Do not edit below

def main():
	query_options = {1: query5(), 6: query6(), 7: query7(), 8: query8(), 
		9: query9(), 10: query10(), 11: query11(), 12: query12(), 13: query13()}
	
	if len(sys.argv) == 1:
		if username() == "username":
			print("Make sure to change the username function to return your username.")
			return
		else:
			print(username())
		for query in query_options.values():
			print(query)
	elif len(sys.argv) == 2:
		if sys.argv[1] == "username":
			print(username())
		else:
			print(query_options[int(sys.argv[1])])

	
if __name__ == "__main__":
   main()
