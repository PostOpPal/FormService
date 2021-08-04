echo "Generating JSON Schemas"
rm generated_models/*.py
mkdir temp
mkdir temp/json_schemas
trap "rm -r temp" Exit
for i in json_schemas/*; do
    nj=${i%.json}
    sudo cat ${nj}.json | jq '.["$id"]' | xargs curl -s > temp/${nj}.json.temp
    cat temp/${nj}.json.temp > ${nj}.json
    nj=${nj#*\/}
    echo "==========================="
    echo "Input file : ${i}"
    json-schema-to-class ${i} -o ./generated_models/${nj}.py --repr
done
wait