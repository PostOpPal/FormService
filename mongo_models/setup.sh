echo "Generating JSON Schemas for Mongo Models"
rm generated_models/*.py
mkdir temp
mkdir temp/json_schemas
trap "rm -r temp" Exit
read -p "Update Schemas y/n "  update
for i in json_schemas/*; do
    nj=${i%.json}
    if [[ "$update" == "y" ]]; then
        sudo cat ${nj}.json | jq '.["$id"]' | xargs curl -s > temp/${nj}.json.temp
        cat temp/${nj}.json.temp > ${nj}.json
    fi
    nj=${nj#*\/}
    echo "Input file : ${i}"
    json-schema-to-class ${i} -o ./generated_models/${nj}.py --repr
done
wait