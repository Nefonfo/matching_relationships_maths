from openpyxl import Workbook

def dictOfCongruence(initial, final, mod):
    dict = set()
    for x in range(initial, final+1):
        for y in range(initial, final+1):
            if ((x-y) % mod == 0):
                dict.add((x,y))
    
    return dict

def excelDict(**kwargs):
    workbookDict = Workbook()
    sheet = workbookDict.active
    for key, value in kwargs.items():
        sheet['{0}{1}'.format(value['cellA'],1)] = 'x - {}'.format(key)
        sheet['{0}{1}'.format(value['cellB'],1)] = 'y - {}'.format(key)
        number = 2
        for dataDict in value['dictionary']:
            sheet['{0}{1}'.format(value['cellA'],number)] = dataDict[0]
            sheet['{0}{1}'.format(value['cellB'],number)] = dataDict[1]
            number = number + 1
    workbookDict.save(filename='results.xlsx')
    print('--- TERMINADO EXITOSAMENTE ---')
            

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
)
    