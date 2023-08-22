
primes=[2];
num=1;
candidate=3;

while (primes.length <= 10001) {
    prime = true;
    //Fermat's primality test
    for(witness=2;witness<=Math.trunc(Math.sqrt(candidate));witness++) {
        if(candidate % witness ==0) {
            prime = false;
            break;
        }
        else if(prime ==true) {
            primes.push(candidate);
            candidate=candidate+2;
        }
    }
}
console.log(candidate);
