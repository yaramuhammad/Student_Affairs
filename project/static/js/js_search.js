function toTitleCase(str)
{
    let names = str.toLowerCase().split(' ')
    let res = "";
    for(let i=0;i<names.length;i++)
    {
        let name = names[i];
        name = name.charAt(0).toUpperCase()+name.substring(1, name.length);
        if(i!==0) res+=" ";
        res+=name;
    }
    return res;
}
function checkLvl(e)
{
    let level = e.parentElement.previousElementSibling.innerHTML;
    if(level!=3)
    {
        alert("Not Eligible");
    }
    else
    {
        let idToAssign = e.parentElement.parentElement.children[1].innerHTML;
        window.location.href = document.querySelector('input[name="dept-url"]').value+`?id=${idToAssign}`;
    }
}

function fill_table(query="All")
{
    var my_url = document.querySelector('input[name="res-url"]').value;

        $.ajax({
            type: 'GET',
            url: my_url,
            data: {
                'query': query,
            },
            dataType: 'json',
            success: function(response)
            {
                let tbdy = document.querySelector('tbody');
                tbdy.innerHTML = '';
                for(let student of response['result'])
                {
                    student['FullName'] = toTitleCase(student['FullName']);
                    let tr = document.createElement('tr');
                    for(let key of ['FullName', 'StudentID', 'StudentLevel'])
                    {
                        let td = document.createElement('td');
                        td.innerHTML = student[key];
                        tr.append(td);
                    }
                    let td = document.createElement('td');
                    td.innerHTML = `<a onclick="checkLvl(this)">ASSIGN DEPARTMENT</a>`
                    tr.append(td);
                    tbdy.append(tr);
                }

            },
            error: function()
            {
                alert("Error");
            }
        });
}
document.addEventListener('DOMContentLoaded', function()
{
    fill_table();
    document.querySelector('#search-button').onclick = function()
    {
        let query = document.querySelector('#search-bar').value;
        fill_table(query);
    };
    let err = document.querySelector('input[name="dept-fail"]');
    if(err)
        alert(err.value)
});