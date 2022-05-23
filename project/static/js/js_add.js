if(!localStorage.getItem('students'))
{
    localStorage.setItem('students', JSON.stringify([]));
}


function ValidateName(nameP)
{
    const letters = /^[A-Za-z]+(\s[A-Za-z]+)+$/;

    if(letters.test(nameP))
        return true;
    else
    {
        alert('Please input alphabet characters only in the Name');
        return false;
    }
}

function ValidateID(ID)
{
    const ident = /^[0-9]{8}$/;
    if(ident.test(ID))
        return true;
    else
    {
        alert("Invalid ID");
        return false;
    }
}

function ValidatePhoneNumber(nom)
{
    if(nom.length>=10 && nom.length<=13)
    {
        return true;
    }
    else{
        alert('Mobile Number Should be Between 10 and 13 Number long');
        return false;
    }
}

function ValidateGPA(gpa)
{
    if (gpa >4 && gpa<0)
    {
        alert('The GPA should be Between "0" and "4" ');
        return false;
    }
    return true
}

function ValidatYear(year)
{
    const d = new Date (year);
    const y = d.getFullYear();
    if (y>1970 && y<9999)
    {
        return true;
    }
    else
    {
        alert('Not A valid Year');
        return false;
    }
}


document.addEventListener("DOMContentLoaded" , function()
{
    document.querySelector("form").onsubmit = function ()
    {
        const name = document.querySelector("#username").value;
        const ID = document.querySelector("#ID").value;
        const gpa = document.querySelector("#gpa").value;
        const mobile = document.querySelector("#mobile").value;
        const datee = document.querySelector("#Date").value;

        let gender = document.querySelector('input[name="gender"]:checked').value;
        let level = document.querySelector("#Level").value;
        let status = document.querySelector('input[name="os"]:checked').value;
        let system = document.querySelector('input[name="system"]:checked').value;
        let depar = document.querySelector('input[name="prog"]').value;
        let email = document.querySelector('input[type="email"]').value;

        if (ValidateName(name) && ValidateID(ID) && ValidatePhoneNumber(mobile) && ValidateGPA(gpa) &&
             ValidatYear(datee))
         {
             // let stu_info = {
             //     "name": name,
             //     "phone": mobile,
             //     "gpa": gpa,
             //     "dob": datee,
             //     "gender": gender,
             //     "level": level,
             //     "status": status,
             //     "system": system,
             //     "department": depar,
             //     "email": email,
             // }
             //
             // //list of IDs of already-registered students
             // // let cur_list = JSON.parse(localStorage.getItem('students'));
             // //
             // // //adding the current student's ID to the list of IDs
             // // cur_list.push(ID);
             // //
             // // //Updating the list in the localStorage
             // // localStorage.setItem('students', JSON.stringify(cur_list));
             // //
             // // //storing the student info using the ID as a key
             // // localStorage.setItem(ID, JSON.stringify(stu_info));
             alert("Student Added Successfully.\n");
             return true;
         }
        return false;
    }
});