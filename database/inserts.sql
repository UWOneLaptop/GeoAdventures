
INSERT INTO Countries (c_id,c_name) VALUES (1,'USA');
INSERT INTO Countries (c_id,c_name) VALUES (2,'Mexico');
INSERT INTO Countries (c_id,c_name) VALUES (3,'Russia');

INSERT INTO Questions (q_id,q_text) VALUES (1,'what is capital?');
INSERT INTO Questions (q_id,q_text) VALUES (2,'what is a burrito?');
INSERT INTO Questions (q_id,q_text) VALUES (3,'what is favorite drink?');

INSERT INTO Answers (q_id,a_text,valid) VALUES (1,'washington dc',1);
INSERT INTO Answers (q_id,a_text,valid) VALUES (2,'a tasty meal',1);
INSERT INTO Answers (q_id,a_text,valid) VALUES (3,'vodka',1);

INSERT INTO Question_Tags (q_id,tag) VALUES (1,'USA');
INSERT INTO Question_Tags (q_id,tag) VALUES (2,'Mexico');
INSERT INTO Question_Tags (q_id,tag) VALUES (3,'Russia');

INSERT INTO Country_Tags (c_id,tag) VALUES (1,'geography');
INSERT INTO Country_Tags (c_id,tag) VALUES (2,'geography');
INSERT INTO Country_Tags (c_id,tag) VALUES (3,'geography');
