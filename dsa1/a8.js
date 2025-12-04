function printNos(n){
    if (n === 0 ) return;
    process.stdout.write(n + "");
    printNos(n - 1 )
}

printNos(10);