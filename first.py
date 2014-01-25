import survey
table = survey.Pregnancies()
table.ReadRecords()
livebirthsfirst = survey.Pregnancies()
livebirthsother = survey.Pregnancies()
for rec in table.records:
    if rec.outcome == 1:
        if rec.birthord == 1:
            livebirthsfirst.AddRecord(rec)
        else:
            livebirthsother.AddRecord(rec)
firstlength = 0
otherlength = 0
for a in livebirthsfirst.records:
    firstlength += a.prglength
for b in livebirthsother.records:
    otherlength += b.prglength
print 'Length of first pregnancies', float(firstlength) / len(livebirthsfirst.records)
print 'Length of other pregnancies', float(otherlength) / len(livebirthsother.records)