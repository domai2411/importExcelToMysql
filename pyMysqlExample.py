import pandas as pd   
import sqlalchemy as sa
from sqlalchemy import exc
connection_url = sa.engine.URL.create(
    "mysql+pymysql",
    username='root',
    password='',
    host='localhost',
    database="testdb"
)
engine = sa.create_engine(connection_url)
connection = engine.connect()
# sourceFile='quiz1.xlsx'

# def createtable(sourceFile):
	# if len(sourceFile) > 0:
		# dataframe = pd.read_excel(
			# sourceFile, 
			# sheet_name=0,
			# header=0)
		# field=list(dataframe)
		# print(field)
	# if "." in sourceFile:
		# table=sourceFile.split(".")[0]
	# else:
		# table=sourceFile
	# sql="CREATE TABLE `"+table+"` ("
	# for f in field:
		
	
def importexcel(sourceFile,tablename):
	print("Reading Scource File "+sourceFile+"...");
	if len(sourceFile) > 0:
		
		sales = pd.read_excel(
			sourceFile, 
			sheet_name=0,
			header=0)
		file = open(tablename+".sql")
		escaped_sql = sa.text(file.read())
		file.close()
		print("Importing TABLE "+tablename+"...");
		try:
			engine.execute("DROP TABLE `"+tablename+"`")
			engine.execute(escaped_sql)
		except exc.SQLAlchemyError as e:
			print(e)
		sales.to_sql( con=engine,name=tablename, if_exists='append', index=False)
		print("Import "+tablename+" Complete")
def runscriptm(scriptfile):
	print("Running File "+scriptfile+"...");
	file = open(scriptfile+".sql")
	sql_all=file.read()
	file.close()
	sqla=sql_all.split(";")
	for sql in sqla:
		sql=sql.strip()
		if sql!="":
			escaped_sql = sa.text(sql)
			try:
				engine.execute(escaped_sql)
			except exc.SQLAlchemyError as e:
				print(e)
	print("SQL Script "+scriptfile+" Complete")
def main():
	sourceFile="quiz1.xlsx"
	tablename="quiz1"
	createtable(sourceFile)
	script="quiz1_script"
	runscriptm(script)
if __name__ == "__main__":
    main()