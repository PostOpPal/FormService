#!/bin/bash

echo "Generating JSON Schemas"
rm -r generated_models/*
mkdir -p temp
mkdir -p temp/json_schemas
trap "rm -r temp" Exit
read -p "Update Schemas y/n "  update
y="y"
link="https://raw.githubusercontent.com/PostOpPal/Schemas/master/"


search_folder () {
    # $1 is the current address
    for item in $1/*; do
        sub_item=${item#*\/}
        if [ -f "${item}" ] ; then
            nj=${sub_item%.json}
            if [[ "$update" == "y" ]]; then
                ending=$(echo -n "${link}" | cat <(echo -n "") - <(cat ${item} | jq '.["$id"]' | sed -e 's/^"//' -e 's/"$//'))
                echo ${ending}.json
                sudo curl -s ${ending}.json > temp/${item}.temp
                cat temp/${item}.temp > ${item}
            fi
            echo "Input file : ${item}"
            datamodel-codegen  --input  ${item} --input-file-type jsonschema --output ./generated_models/${nj}.py
        fi
        if [ -d "${item}" ] ; then
            mkdir -p generated_models/${sub_item}
            mkdir -p temp/${item}
            search_folder ${item}
        fi
    done
}

search_folder json_schemas

wait