import sqlite3 as lite
import sys,csv

con = None

try:
    con = lite.connect('countries.db')
    
    cur = con.cursor()    
    cur.execute('select * from country')
    
    for row in cur:
        print row

    cur.execute('DROP TABLE country')
    cur.execute('CREATE TABLE IF NOT EXISTS country (territory VARCHAR,totalkm VARCHAR,totalsqmi VARCHAR,landkm2 VARCHAR,landsqmi VARCHAR,waterkm2 VARCHAR,watersqmi VARCHAR,perwater VARCHAR,Christian VARCHAR,Muslim VARCHAR,Buddhist VARCHAR,Hindu VARCHAR,Others VARCHAR,Nonreligious VARCHAR,Population VARCHAR,CountryCode VARCHAR,LongName VARCHAR,Region VARCHAR,IncomeGroup VARCHAR,CurrencyUnit VARCHAR,Constitutionalform VARCHAR,Headofstate VARCHAR,Basisofexecutivelegitimacy VARCHAR)')

    reader = csv.reader(open('countryfactsv2.csv', "rb"))
    for territory,totalkm,totalsqmi,landkm2,landsqmi,waterkm2,watersqmi,perwater,Christian,Muslim,Buddhist,Hindu,Others,Nonreligious,Population,CountryCode,LongName,Region,IncomeGroup,CurrencyUnit,Constitutionalform,Headofstate,Basisofexecutivelegitimacy,null in reader:
        print territory
        cur.execute('INSERT OR IGNORE INTO country (territory,totalkm,totalsqmi,landkm2,landsqmi,waterkm2,watersqmi,perwater,Christian,Muslim,Buddhist,Hindu,Others,Nonreligious,Population,CountryCode,LongName,Region,IncomeGroup,CurrencyUnit,Constitutionalform,Headofstate,Basisofexecutivelegitimacy) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (unicode(territory),unicode(totalkm),unicode(totalsqmi),unicode(landkm2),unicode(landsqmi),unicode(waterkm2),unicode(watersqmi),unicode(perwater),unicode(Christian),unicode(Muslim),unicode(Buddhist),unicode(Hindu),unicode(Others),unicode(Nonreligious),unicode(Population),unicode(CountryCode),unicode(LongName),unicode(Region),unicode(IncomeGroup),unicode(CurrencyUnit),unicode(Constitutionalform),unicode(Headofstate),unicode(Basisofexecutivelegitimacy)))
        con.commit()

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
