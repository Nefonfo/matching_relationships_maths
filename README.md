# MATCHING RELATIONSHIPS #
### only linear sequences without jumps ## 


## INSTRUCTIONS ##

### Step 1 ###
Install the requirements
<pre><code> pip install -r requiments.txt </code></pre>

### Step 2 ###

Modify the parameters to pass to the function (unlimited but check that the cell 'cellA' and 'cellB' are different from all the others)

Example:

```python
excelDict(
    mod3 = {
        'dictionary': dictOfCongruence(0,12,3),
        'cellA': 'A',
        'cellB': 'B'
    },
    mod5 = {
        'dictionary': dictOfCongruence(0,12,5),
        'cellA': 'C',
        'cellB': 'D'
    }
    # (it will be the same name in the cell 'x - name')
    name = {
        'dictionary': dictOfCongruence(firstNumber,LastNumber,Mod),
        'cellA': 'CELL_E-???',
        'cellB': 'CELL_F - ???'
    }
)
```

### Step 3 ###
Execute code:
<pre><code>python MatematicasDisc.py</code></pre>