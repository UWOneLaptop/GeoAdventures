CREATE TABLE Answers (q_id INTEGER, a_text TEXT,
			valid INTEGER, 
			FOREIGN KEY (q_id) REFERENCES Questions (q_id));


CREATE TABLE Countries (c_id INTEGER, 
			c_name TEXT, 
			PRIMARY KEY (c_id)
			UNIQUE(c_name));


CREATE TABLE Questions (
q_id INTEGER,

			q_text TEXT,
			
PRIMARY KEY (q_id));


CREATE TABLE Question_Tags  (q_id INTEGER, 
				tag TEXT,
FOREIGN KEY (q_id) REFERENCES Questions (q_id));


CREATE TABLE Country_Tags  (c_id INTEGER, tag TEXT, 
				FOREIGN KEY (c_id) REFERENCES Country (c_id));

