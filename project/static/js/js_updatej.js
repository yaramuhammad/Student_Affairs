/*Default Display of Table Data*/
//#########################################################################

/*---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- */
/*Delete Function */
/*---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- */
/*Search Filter*/

/*---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- */
/* pop-up form*/
// function toTitleCase(str)
// {
//     let names = str.toLowerCase().split(' ')
//     let res = "";
//     for(let i=0;i<names.length;i++)
//     {
//         let name = names[i];
//         name = name.charAt(0).toUpperCase()+name.substring(1, name.length);
//         if(i!==0) res+=" ";
//         res+=name;
//     }
//     return res;
// }
//
//  function addRow(stud_info, cntr)
// {
//     //alert(stud_info)
//     let tbdy = document.querySelector('tbody');
//     let tr = document.createElement("tr");
//       for(let j=0;j<9;j++)
//       {
//           let td = document.createElement("td");
//           //counter
//           if(j===0)
//           {
//               td.innerHTML = cntr;
//               td.className = "narrow";
//           }
//           //name
//           else if(j===1)
//           {
//               td.innerHTML = toTitleCase(stud_info["FullName"]);
//               td.className = "name";
//           }
//           //id
//           else if(j===2)
//           {
//               td.innerHTML = stud_info['StudentID'];
//               td.className = "wide";
//           }
//           //dept
//           else if(j===3)
//           {
//               td.innerHTML = stud_info["Department"];
//               td.className = "narrow";
//           }
//           //status
//           else if(j===4)
//           {
//               td.innerHTML = stud_info["Status"];
//               td.className = "wide";
//           }
//           //gpa
//           else if(j===5)
//           {
//               td.innerHTML = stud_info["Gpa"];
//               td.className = "narrow";
//           }
//           //year
//           else if(j===6)
//           {
//               td.innerHTML = stud_info["StudentLevel"];
//               td.className = "narrow";
//           }
//           //system
//           else if(j===7)
//           {
//               td.innerHTML = stud_info["System"];
//               td.className = "narrow";
//           }
//           else
//           {
//               td.innerHTML = `<button class="button edit" onclick="openForm(this)"><i class='fa fa-edit' style="font-size:30px; color: blue;"></i></button> <button onclick = "del_func(this)" class="button delete"><i class="fa fa-trash-o" style="font-size:30px;color:red"></i></button>`
//               td.className = "actions";
//           }
//           tr.appendChild(td);
//       }
//       tbdy.appendChild(tr);
// }

// function fill_table(query="All", filterAttr='All', filterVal=0)
// {
//     var my_url = document.querySelector('input[name="res-url"]').value;
//
//         $.ajax({
//             type: 'GET',
//             url: my_url,
//             data: {
//                 'query': query,
//                 'filterAttr': filterAttr,
//                 'filterVal':filterVal,
//             },
//             dataType: 'json',
//             success: function(response)
//             {
//                 let result = response['result']
//                 for(let i=0; i<result.length;i++)
//                     addRow(result[i], i+1)
//
//             },
//             error: function()
//             {
//                 alert("Error");
//             }
//         });
// }
//

/*###########################################################################################################################*/
function openForm(elem)
{
    document.getElementById("myForm").style.display = "block";
    stud_info = elem.parentElement.parentElement.children;
    document.querySelector('input[name="Name"]').value = stud_info[1].innerHTML;
    document.querySelector('input[name="ID"]').value = stud_info[2].innerHTML;
    document.querySelector('#status-slider').checked = stud_info[4].innerHTML === "Active";
    document.querySelector('#level-select').value = stud_info[6].innerHTML;
    document.querySelector('input[name="GPA"]').value = stud_info[5].innerHTML;
    document.querySelector('#system-select').value = stud_info[7].innerHTML;
}
function gpa_adj(gpa)
{
    return gpa.charAt(0) + gpa.charAt(1) + gpa.charAt(2);
}
function del_func(elem)
    {
        if (window.confirm('Are You Sure You Want To Delete This Student?'))
        {
            let id_to_del = elem.parentElement.parentElement.children[2].innerHTML;
            let del_url = document.querySelector('input[name="del-url"]').value;

            $.ajax({
                type: 'GET',
                url: del_url,
                data: {
                    'id_to_del': id_to_del,
                },
                success: function(response)
                {
                    alert(response);
                    window.location.reload();
                },
                error: function()
                {
                    alert("Error During Deletion.");
                }
            });
        }
    }
    function myFunction() {
    // Declare variables
    // var input, table, tr, i, txtValue;
    // input = document.getElementById('myInput').value;
    // table = document.getElementById("table");
    // tr = document.getElementsByClassName('name');
    //
    // for (i = 0; i < tr.length; i++)
    // {
    //   txtValue = tr.textContent || tr.innerText;
    //
    //   if (txtValue.indexOf('input') > -1)
    //   {
    //     tr[i].style.display = "";
    //   }
    //   else
    //   {
    //     tr[i].style.display = "none";
    //   }
    // }
    }
    function closeForm() {
    document.getElementById("myForm").style.display = "none";
    }
document.addEventListener('DOMContentLoaded', function()
{
    document.querySelector('#edit-form').onsubmit = function()
    {
        let newName = document.querySelector('input[name="Name"]').value;
        let newID = document.querySelector('input[name="ID"]').value;
        let newStatus = document.querySelector('#status-slider').checked;
        let newLevel = document.querySelector('#level-select').value;
        let newGPA = gpa_adj(document.querySelector('#gpa').value);
        let newSys = document.querySelector('#system-select').value;
        if(newStatus) newStatus = 'Active';
        else newStatus = 'InActive';
        let new_stud = {
                    'FullName': newName,
                    'StudentID': newID,
                    'Status': newStatus,
                    'StudentLevel': newLevel,
                    'Gpa': newGPA,
                    'System': newSys,
                }

        let edit_url = document.querySelector('input[name="edit-url"]').value;
        let old_id = document.querySelector('input[name="old_stud_id"]').value;

        $.ajax({
            type: 'GET',
            url: edit_url,
            data:{
                'student': JSON.stringify(new_stud),
            },
            success: function(response)
            {
                alert('Edited Successfully.');
                window.location.href = document.querySelector('input[name="this-page-url"]').value;
            },
            error: function(response)
            {
                alert('Editing Error.');
            }
        });
        window.location.reload();
    }

    window.onclick = function(event)
    {
    var form = document.getElementById("myForm");
    if (event.target == form)
        form.style.display = "none";
    }
});
