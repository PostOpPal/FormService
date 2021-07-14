echo "======================================================"
echo "Building SQLAlchemy Models"
rm -f temp.db
sqlite3 temp.db < schema.sql
sqlacodegen  sqlite:///temp.db > ./models.py
rm temp.db
#replace the declerative base stuff in the generated models to match the use of db.model
sed -i 's/from sqlalchemy\.ext\.declarative import declarative_base/ /g' models.py
sed -i 's/Base = declarative_base()/ /g' models.py
sed -i 's/metadata = Base.metadata/ /g' models.py
sed -i 's/Base/db\.Model/g' models.py
echo 'from app import db \n' | cat - models.py > temp && mv temp models.py