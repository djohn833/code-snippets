from collections import defaultdict
from itertools import product
import random
import time


tenses = ['Present', 'Imperfect', 'Future', 'Perfect', 'Pluperfect', 'Future Perfect']
forms = ['1st Sg.', '2nd Sg.', '3rd Sg.', '1st Pl.', '2nd Pl.', '3rd Pl.']
moods = ['Indicative Active', 'Indicative Passive', 'Subjunctive Active', 'Subjunctive Passive']
moods_forms = list(product(moods, forms))

verbs = defaultdict(list)

amo_table = '''amō	amābam	amābō	amāvī	amāveram	amāverō
amās	amābās	amābis	amāvistī	amāverās	amāveris
amat	amābat	amābit	amāvit	amāverat	amāverit
amāmus	amābāmus	amābimus	amāvimus	amāverāmus	amāverimus
amātīs	amābātis	amābitis	amāvistis	amāverātis	amāveritis
amant	amābant	amābunt	amāvērunt	amāverant	amāverint
amor	amābar	amābor	amātus sum	amātus eram	amātus erō
amāris	amābāris	amāberis	amātus es	amātus erās	amātus eris
amātur	amābātur	amābitur	amātus est	amātus erat	amātus erit
amāmur	amābāmur	amābimur	amātī sumus	amātī erāmus	amātī erimus
amāminī	amābāminī	amābiminī	amātī estis	amātī erātis	amātī eritis
amantur	amābantur	amābuntur	amātī sunt	amātī erant	amātī erunt
amem	amārem		amāverim	amāvissem	
amēs	amārēs		amāveris	amāvissēs	
amet	amāret		amāverit	amāvisset	
amēmus	amārēmus		amāverimus	amāvissēmus	
amētis	amārētis		amāveritis	amāvissētis	
ament	amārent		amāverint	amāvissent	
amer	amārer		amātus sim	amātus essem	
amēris	amārēris		amātus sīs	amātus essēs	
amētur	amārētur		amātus sit	amātus esset	
amēmur	amārēmur		amātī sīmus	amātī essēmus	
amēminī	amārēminī		amātī sītis	amātī essētis	
amentur	amārentur		amātī sint	amātī essent	'''

moneo_table = '''moneō	monēbam	monēbō	monuī	monueram	monuerō
monēs	monēbās	monēbis	monuistī	monuerās	monueris
monet	monēbat	monēbit	monuit	monuerat	monuerit
monēmus	monēbāmus	monēbimus	monuimus	monuerāmus	monuerimus
monētis	monēbātis	monēbitis	monuistis	monuerātis	monueritis
monent	monēbant	monēbunt	monuērunt	monuerant	monuerint
moneor	monēbar	monēbor	monitus sum	monitus eram	monitus erō
monēris	monēbāris	monēberis	monitus es	monitus erās	monitus eris
monētur	monēbātur	monēbitur	monitus est	monitus erat	monitus erit
monēmur	monēbāmur	monēbimur	monitī sumus	monitī erāmus	monitī erimus
monēminī	monēbāminī	monēbiminī	monitī estis	monitī erātis	monitī eritis
monentur	monēbantur	monēbuntur	monitī sunt	monitī erant	monitī erunt
moneam	monērem		monuerim	monuissem	
moneās	monērēs		monueris	monuissēs	
moneat	monēret		monuerit	monuisset	
moneāmus	monērēmus		monuerimus	monuissēmus	
moneātis	monērētis		monueritis	monuissētis	
moneant	monērent		monuerint	monuissent	
monear	monērer		monitus sim	monitus essem	
moneāris	monērēris		monitus sīs	monitus essēs	
moneātur	monērētur		monitus sit	monitus esset	
moneāmur	monērēmur		monitī sīmus	monitī essēmus	
moneāminī	monērēminī		monitī sītis	monitī essētis	
moneantur	monērentur		monitī sint	monitī essent	'''

duco_table = '''dūcō	dūcēbam	dūcam	dūxī	dūxeram	dūxerō
dūcis	dūcēbās	dūcēs	dūxistī	dūxerās	dūxeris
dūcit	dūcēbat	dūcet	dūxit	dūxerat	dūxerit
dūcimus	dūcēbāmus	dūcēmus	dūximus	dūxerāmus	dūxerimus
dūcitis	dūcēbātis	dūcētis	dūxistis	dūxerātis	dūxeritis
dūcunt	dūcēbant	dūcent	dūxērunt	dūxerant	dūxerint
dūcor	dūcēbar	dūcar	ductus sum	ductus eram	ductus erō
dūceris	dūcēbāris	dūcēris	ductus es	ductus erās	ductus eris
dūcitur	dūcēbātur	dūcētur	ductus est	ductus erat	ductus erit
dūcimur	dūcēbāmur	dūcēmur	ductī sumus	ductī erāmus	ductī erimus
dūciminī	dūcēbāminī	dūcēminī	ductī estis	ductī erātis	ductī eritis
dūcuntur	dūcēbantur	dūcentur	ductī sunt	ductī erant	ductī erunt
dūcam	dūcerem		dūxerim	dūxissem	
dūcās	dūcerēs		dūxeris	dūxissēs	
dūcat	dūceret		dūxerit	dūxisset	
dūcāmus	dūcerēmus		dūxerimus	dūxissēmus	
dūcātis	dūcerētis		dūxeritis	dūxissētis	
dūcant	dūcerent		dūxerint	dūxissent	
dūcar	dūcerer		ductus sim	ductus essem	
dūcāris	dūcerēris		ductus sīs	ductus essēs	
dūcātur	dūcerētur		ductus sit	ductus esset	
dūcāmur	dūcerēmur		ductī sīmus	ductī essēmus	
dūcāminī	dūcerēminī		ductī sītis	ductī essētis	
dūcantur	dūcerentur		ductī sint	ductī essent	'''

incipio_table = '''incipiō	incipiēbam	incipiam	incēpī	incēperam	incēperō
incipis	incipiēbās	incipiēs	incēpistī	incēperās	incēperis
incipit	incipiēbat	incipiet	incēpit	incēperat	incēperit
incipimus	incipiēbāmus	incipiēmus	incēpimus	incēperāmus	incēperimus
incipitis	incipiēbātis	incipiētis	incēpistis	incēperātis	incēperitis
incipiunt	incipiēbant	incipient	incēpērunt	incēperant	incēperint
incipior	incipiēbar	incipiar	inceptus sum	inceptus eram	inceptus erō
inciperis	incipiēbāris	incipiēris	inceptus es	inceptus erās	inceptus eris
incipitur	incipiēbātur	incipiētur	inceptus est	inceptus erat	inceptus erit
incipimur	incipiēbāmur	incipiēmur	inceptī sumus	inceptī erāmus	inceptī erimus
incipiminī	incipiēbāminī	incipiēminī	inceptī estis	inceptī erātis	inceptī eritis
incipiuntur	incipiēbantur	incipientur	inceptī sunt	inceptī erant	inceptī erunt
incipiam	inciperem		incēperim	incēpissem	
incipiās	inciperēs		incēperis	incēpissēs	
incipiat	inciperet		incēperit	incēpisset	
incipiāmus	inciperēmus		incēperimus	incēpissēmus	
incipiātis	inciperētis		incēperitis	incēpissētis	
incipiant	inciperent		incēperint	incēpissent	
incipiar	inciperer		inceptus sim	inceptus essem	
incipiāris	inciperēris		inceptus sīs	inceptus essēs	
incipiātur	inciperētur		inceptus sit	inceptus esset	
incipiāmur	inciperēmur		inceptī sīmus	inceptī essēmus	
incipiāminī	inciperēminī		inceptī sītis	inceptī essētis	
incipiantur	inciperentur		inceptī sint	inceptī essent	'''

audio_table = '''audiō	audiēbam	audiam	audīvī	audīveram	audīverō
audīs	audiēbās	audiēs	audīvistī	audīverās	audīveris
audit	audiēbat	audiet	audīvit	audīverat	audīverit
audīmus	audiēbāmus	audiēmus	audīvimus	audīverāmus	audīverimus
audītis	audiēbātis	audiētis	audīvistis	audīverātis	audīveritis
audiunt	audiēbant	audient	audīvērunt	audīverant	audīverint
audior	audiēbar	audiar	audītus sum	audītus eram	audītus erō
audīris	audiēbāris	audiēris	audītus es	audītus erās	audītus eris
audītur	audiēbātur	audiētur	audītus est	audītus erat	audītus erit
audīmur	audiēbāmur	audiēmur	audītī sumus	audītī erāmus	audītī erimus
audīminī	audiēbāminī	audiēminī	audītī estis	audītī erātis	audītī eritis
audiuntur	audiēbantur	audientur	audītī sunt	audītī erant	audītī erunt
audiam	audīrem		audīverim	audīvissem	
audiās	audīrēs		audīveris	audīvissēs	
audiat	audīret		audīverit	audīvisset	
audiāmus	audīrēmus		audīverimus	audīvissēmus	
audiātis	audīrētis		audīveritis	audīvissētis	
audiant	audīrent		audīverint	audīvissent	
audiar	audīrer		audītus sim	audītus essem	
audiāris	audīrēris		audītus sīs	audītus essēs	
audiātur	audīrētur		audītus sit	audītus esset	
audiāmur	audīrēmur		audītī sīmus	audītī essēmus	
audiāminī	audīrēminī		audītī sītis	audītī essētis	
audiantur	audīrentur		audītī sint	audītī essent	'''


def add_table(verb, table):
  for (mood, form), line in zip(moods_forms, table.splitlines()):
    for tense, text in zip(tenses, line.split("\t")):
      if text:
        verbs[text].append(' '.join((verb, mood, tense, form)))


add_table('amō', amo_table)
add_table('moneō', moneo_table)
add_table('dūcō', duco_table)
add_table('incipiō', incipio_table)
add_table('audiō', audio_table)

items = list(verbs.items())

question, answer = random.choice(items)
answer = "\n".join(answer)

print(question)
response = input()
if response == answer:
  print('Correct!')
else:
  print('Incorrect!')
  print(answer)
