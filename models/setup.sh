echo "Generating JSON Schemas"
mkdir temp
mkdir temp/json_schemas
trap "rm -r temp" Exit
for i in json_schemas/*; do
    nj=${i%.json}
    #echo ${nj}.json
    #cat ${nj}.json | echo
    #echo cat ${nj}.json | jq '.["$id"]'
    sudo cat ${nj}.json | jq '.["$id"]' | xargs curl -s > temp/${nj}.json.temp
    cat temp/${nj}.json.temp > ${nj}.json
    #rm ${nj}.json.temp
    nj=${nj#*\/}
    echo "==========================="
    echo "Input file : ${i}"
    json-schema-to-class ${i} -o ./generated_models/${nj}.py --repr
    #rm ${nj}.json.temp
done
wait