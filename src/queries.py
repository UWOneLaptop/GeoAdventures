"""
This file defines a set of queries for interaction with the database. Each
function in this file returns a SQL query that should be executed by te python code.
"""

def query_countries():
    """
    Returns a query that select all the countries from the database
    """
    return "SELECT * FROM Countries;"

def get_tags(country_id):
    """
    Returns a query that selects all the tags associated with country from
    the database

    accepts integer parameter corresponding to the country id
    """
    return "SELECT tag FROM Country_Tags WHERE c_id = "+str(country_id)+";"

def get_answers_by_q_id(q_id):
    return "SELECT DISTINCT a.a_text, a.valid FROM Answers a \
    WHERE a.q_id = " + str(q_id) + " ;"
    
def get_question_by_tag(tag):
    """
    Returns a SQL query that selects all the questions associated with a specific
    tag

    accepts string tag
    """
    return "SELECT q.q_id, q.q_text FROM Questions q, Question_Tags qt \
            WHERE q.q_id = qt.q_id \
            AND qt.tag = '" + tag + "';"

#TODO optimize this using nested Query perhaps
def get_question_by_tags(tags):
    i = 0;
    query_top = "SELECT * FROM Questions q  "
    query_bottom = "WHERE "
    for tag in tags:
        tag_instance = "qt"+str(i)    
        query_top += ", Question_Tags " + tag_instance + " "
        query_bottom += ("q.q_id  = " + tag_instance + ".q_id " +
        "AND " + tag_instance + ".tag = '" + tag +"' AND ")

        i+=1
    query_top += query_bottom[0:-5]
    print(query_top)
    return query_top
                 
             
