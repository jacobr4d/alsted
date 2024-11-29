import sys

def bq(p):
    l=p.split('\n')
    for i in range(len(l)):
        if l[i].startswith('    '):
            l[i]='<span>'+l[i]+'</span>'
    return '\n'.join(l)

a,b=sys.argv[1:3]
a,b=map(lambda x:open(x).read().split('\n\n'),[a,b])
assert(len(a)==len(b))
print('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Document</title>
<style>
    body {
        # background: #fff6d5;
    }
    table {
        border-collapse: separate; 
        border-spacing: 1em;
    }
    span {
        display: block;
        margin-left: 1em;
    }
</style>
</head>
<body>
<table>
<tbody>''')
for a,b in zip(a,b):
    a,b=bq(a),bq(b)
    print('<tr><td onclick="selectText(event)">'+a+'</td><td onclick="selectText(event)">'+b+'</td></tr>')
print('''</tbody>
</table>
<script>
function selectText(event) {
    if (event.detail !== 3) return;
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(event.currentTarget);
    selection.removeAllRanges();
    selection.addRange(range);
}
</script>
</body>
</html>''')