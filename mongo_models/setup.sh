echo "Generating JSON Schemas"
for i in json_schemas/*; do

    nj=${i%.json}
    nj=${nj#*\/}
    echo "==========================="
    echo "Input file : ${i}"
    json-schema-to-class ${i} -o ./generated_models/${nj}.py --repr
done