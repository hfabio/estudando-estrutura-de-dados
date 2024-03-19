/**
Escrever um algoritmo para contar quantos bits foram usados em uma sequência até um certo número. Ex:
dado um número 5, contar os bits usados na sequência de 0, 1, 2, 3, 4, 5
0  = 00000000 = 0
1  = 00000001 = 1
2  = 00000010 = 1
3  = 00000011 = 2
4  = 00000100 = 1
5  = 00000101 = 2
solução = [0, 1, 1, 2, 1, 2]
*/
class Solution {
    countBits(number){
        const bits = [];
        while(number > -1){
            let temp = number;
            let count = 0;
            while(temp){
                count += temp & 1 // & = bitwise and, tabela verdade AND, 1 e 1 = true, 1 e 0 = false, 0 e 1 = false e 0 e 0 = false
                temp = temp >> 1 // >> 1 = bitwise right shift, num byte "empurra uma casa a direita". 00000010 vira 00000001 
            }
            bits.push(count);
            number--;
        }
        return bits.reverse();
    }
}

console.log(new Solution().countBits(5));
