// https://leetcode.com/problems/transpose-matrix/

var transpose = function(matrix) {
    let new_num_rows = matrix[0].length;
    let new_matrix = [];

    for (let i = 0; i < matrix[0].length; i++) {
        let temp_row = [];
        for (let j = 0; j < matrix.length; j++) {
            temp_row.push(matrix[j][i])
        }
        new_matrix.push(temp_row);
    }
    return new_matrix;
    
};
