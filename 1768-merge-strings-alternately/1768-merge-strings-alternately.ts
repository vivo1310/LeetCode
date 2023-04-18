function mergeAlternately(word1: string, word2: string): string {
    let result = []
    for (let i = 0; i < Math.max(word1.length, word2.length); i++) {
        i >= word1.length ? result.push('') : result.push(word1[i])
        i >= word2.length ? result.push('') : result.push(word2[i])
    }
    return result.join('')
};