base="https://api.pokemontcg.io/v1/cards?setCode="
page="&page="
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
FILE="setcodes.txt"
IN="$DIR/$FILE"

echo "Installing"
exit

while read p;
do
    pg=1;
    for run in {1..4}
    do
        echo "reading $p, page $pg";
        curl $base$p$page$pg > "../local-storage/$p-$pg".json;
        ((pg++));
    done
done < $IN
