base="https://api.pokemontcg.io/v1/cards?setCode="
page="&page="
while read p;
do
    pg=1;
    for run in {1..4}
    do
        echo "reading $p, page $pg";
        curl $base$p$page$pg > "cards/$p-$pg".json;
        ((pg++));
    done
done < setcodes.json
