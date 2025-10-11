let numbers = [];


for (let i = 0; i <200; i++){
    numbers.push(i)
}


for (let n of numbers){
    if (n % 2 === 0){
        console.log(n + '  is even');
    }else
    {
        console.log(n + '  is odd');    
    }
}