// 1. Student Grade Calculator


let students = [

    {
        name : "Ajay",
        marks : [56, 70, 80 ,90, 78] 
    }, 
    {
        name : "eniyan",
        marks : [10, 20, 45, 60, 100]

    },
    {
        name : "anirudh",
        marks : [56, 70, 80, 90, 100]
    }

]

function StudentGradeCal(students_arr){

    let students_score_arr= []

    for (let i = 0 ; i < students_arr.length ; i++){
        let std_name = students_arr[i].name;
        let std_marks = students_arr[i].marks;

        let std_total_marks = std_marks.reduce((total,num) => total + num,0);
        let average = std_total_marks/std_marks.length;

        let grade = "";

        if (average >= 90) {
            grade = "A";
        }
        else if (average >= 70){
            grade = "B";
        }
        else if (average >= 50){
            grade = "C";
        }
        else {
            grade = "F";
        }

        students_score_arr.push({
            name : std_name,
            totalMarks : std_total_marks,
            averageMarks : average,
            grade : grade,
        })
}
    return students_score_arr

}

console.log(StudentGradeCal(students))
