import math
monkeys = []

with open('in') as f:
    for l in f.read().splitlines():
        if len(l) == 0:
            continue
        if l.startswith('Monkey'):
            monkeys.append({})
            continue
        cur = monkeys[-1]
        if l.startswith('  Starting items:'):
            q = len('  Starting items: ')
            f = [int(c.replace(',', '')) for c in l[q:].split(' ')]
            cur['si'] = f
        if l.startswith('  Operation: '):
            q = len('  Operation: new = ')
            cur['op'] = l[q:].split(' ')
        if l.startswith('  Test: divisible by '):
            cur['amt'] = int(l.split(' ')[-1])
        if l.startswith('    If true: throw to monkey'):
            cur['true'] = int(l.split(' ')[-1])
        if l.startswith('    If false: throw to monkey'):
            cur['false'] = int(l.split(' ')[-1]) 
        # print(cur)

# print(monkeys)



for rd in range(20):
    for m in monkeys:
        for item in m['si']:
            m['ct'] = m.get('ct', 0) + 1
            op = m['op'].copy()
            for i in range(3):
                if op[i] == 'old':
                    op[i] = item
            for i in range(3):
                try:
                    op[i] = int(op[i])
                except:
                    pass
            if op[1] == '+':
                w = op[0] + op[2]
            elif op[1] == '-':
                w = op[0] - op[2]
            elif op[1] == '*':
                w = op[0] * op[2]
            w //= 3
            if w % m['amt'] == 0:
                monkeys[m['true']]['si'].append(w)
            else:
                monkeys[m['false']]['si'].append(w)
            m['si'] = m['si'][1:]

l = sorted(list(m['ct'] for m in monkeys))
print(l[-1] * l[-2])