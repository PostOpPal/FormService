echo "Generating JSON Schemas"
rm -f generated_models/*.py
mkdir -p temp
mkdir -p temp/json_schemas
trap "rm -r temp" Exit
for folder in json_schemas/*; do
    #echo ${folder}
    sub_folder=${folder#*\/}
    #echo ${sub_folder}
    mkdir generated_models/${sub_folder}
    mkdir -p temp/${folder}
    mkdir -p generated_models
    for i in ${folder}/*; do
        nj=${i%.json}
        sudo cat ${nj}.json | jq '.["$id"]' | xargs curl -s > temp/${nj}.json.temp
        cat temp/${nj}.json.temp > ${nj}.json
        nj=${nj#*\/}
        #echo "==========================="
        echo "Input file : ${i}"
        json-schema-to-class ${i} -o ./generated_models/${nj}.py --repr
    done
done
wait