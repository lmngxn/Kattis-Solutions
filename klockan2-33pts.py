# The Clock
# I "deleted" something so that this one is not full 100/100 but only 33/100
# please fully understand the task to "fix" the issue (or review the recording)

desired_a = int(input())
for hh in range(12):
    for mm in range(60):
        h_a = hh*3600//12 + mm*5
        m_a = mm*3600//60
        a = m_a - h_a
        if a == desired_a:
            print('%02d:%02d' % (hh, mm))

# PS: There is an alternative formulaic solution too, i.e., given desired_a(ngle) as input, we know immediately what is hh and mm without trying all possibilities