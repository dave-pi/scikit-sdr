import logging

import numpy as np
import sksdr

_log = logging.getLogger(__name__)

def test_freq_sync():
    mod = sksdr.QPSK
    sps = 2
    damp_factor = 1.0
    norm_loop_bw = 0.01
    fsync = sksdr.FrequencySync(mod, sps, damp_factor, norm_loop_bw)

    in_frame = np.array([
       -0.00001940952177043791-0.000015698909952685536j,
        0.00045504183194606325-0.00013286298404358807j ,
       -0.00042450747486277374-0.00025437545501390973j ,
        0.00019239094238467552+0.0004612717535677375j  ,
        0.0004005268495389987 -0.001320052406364037j   ,
       -0.0006255110024933941 +0.0013039071239998156j  ,
        0.00040400059521223514-0.002459701329391876j   ,
       -0.002193873381528496  +0.002004500832185964j   ,
        0.013938775664589178  +0.009039323239035717j   ,
       -0.01367352470092345   -0.021573839374980825j   ,
       -0.1241527695385146    -0.006959029093523439j   ,
       -0.17058745936957068   +0.09600289150181793j    ,
       -0.05796136981096818   +0.12195261559481316j    ,
        0.03646143030544528   +0.002516369280325701j   ,
       -0.013771997783866192  -0.05584572781021223j    ,
       -0.08844593795522468   -0.02763232994211465j    ,
       -0.13235076438032103   -0.06377781306029459j    ,
       -0.11063509790209256   -0.06459042748787186j    ,
       -0.06262295436437225   +0.138934422233517j      ,
       -0.12782058476305425   +0.7073642559403253j     ,
       -0.1480949572650813    +1.4211091446564759j     ,
       -0.0289111442112015    +1.6827692345314458j     ,
        0.09833784404116097   +1.4834323806505185j     ,
        0.09520928170466159   +1.2838866497032693j     ,
       -0.02743850947903237   +1.3616351181494413j     ,
       -0.07659893281204469   +1.4283007854458598j     ,
       -0.35962018619854713   +1.504550814173098j      ,
       -0.5817408720687084    +1.9630558749498046j     ,
       -0.19455647738170845   +1.6289567833413203j     ,
        0.10016340211805039   -0.038501884294428745j   ,
        0.26053068908813887   -1.6215984351197743j     ,
        0.5024170490629329    -2.357815223846675j      ,
        0.24814738018205573   -1.9092638873185672j     ,
       -0.20901883977860652   -0.37066685691608947j    ,
       -0.3179534555019314    +1.2936734465909183j     ,
       -0.0826302433072111    +2.2882506237900526j     ,
        0.34596099439295874   +1.8084267016654265j     ,
        0.5413188709885303    -0.12867156182060166j    ,
        0.030334002829854434  -1.3312915371300473j     ,
       -0.7661084369400554    -0.053604148598742074j   ,
       -0.5691587278255932    +1.401404863984715j      ,
        0.3710782050985902    +0.166098463688894j      ,
        0.4090308834810661    -1.524931528887686j      ,
       -0.2740548501121128    -0.47501099859591167j    ,
       -0.07899964215776856   +1.6532723916833658j     ,
        1.0618489463608949    +1.8768620816776524j     ,
        1.644848130500093     +0.339915043994172j      ,
        1.0463363393298253    -1.2243857231508852j     ,
        0.5489656000176586    -1.723963088026756j      ,
        1.082310301652007     -1.0498074259364731j     ,
        1.5173478017854367    +0.13380396789721705j    ,
        0.8460656334565588    +1.05721842498742j       ,
       -0.09821747460074448   +1.550413547257735j      ,
       -0.3202856587805455    +1.7333963223222073j     ,
       -0.2980759832720994    +1.488130563910461j      ,
       -0.7858560686897625    +0.7582128076675567j     ,
       -1.3361974852817846    -0.20732266440430513j    ,
       -1.1101926246512277    -1.059255549154638j      ,
       -0.1556750856631297    -1.3555850679774792j     ,
        0.8292864380569747    -0.7826217289436926j     ,
        1.3131363477263172    +0.1115385361572635j     ,
        0.8707541957099734    +0.5377795350353908j     ,
       -0.0785295598918283    +0.9574307521698318j     ,
       -0.25600430983534495   +1.5779236743941056j     ,
       -0.002123033811116115  +1.3573754818628687j     ,
       -0.575115860737733     +0.45873568374374146j    ,
       -1.3110887974749859    -0.005842460356188739j   ,
       -1.3207413884073242    -0.02862091744666795j    ,
       -1.2568595966017777    +0.06997939707661005j    ,
       -1.460257718238804     +0.21123810392610737j    ,
       -1.2704071170582432    -0.011591771770037486j   ,
       -0.477961061111977     -0.7355668550796323j     ,
        0.34718422855889813   -1.255589255934894j      ,
        0.8420334100220701    -0.8803199564157523j     ,
        1.0070821153359202    +0.11008987942734794j    ,
        0.678512845329849     +0.962438379806064j      ,
       -0.007026993080943955  +1.2559448071354367j     ,
       -0.641576636759757     +0.806896299477998j      ,
       -1.1010520414859462    +0.10997214653231074j    ,
       -1.1941866718466985    -0.1915362095531998j     ,
       -0.9483328597748741    -0.00040452692869486634j ,
       -0.528978152308057     +0.6412109699052535j     ,
       -0.28792427123675      +0.9368401856093288j     ,
       -0.7829425697849685    +0.39866736132308395j    ,
       -0.9837185895586921    -0.09153157854837451j    ,
        0.13779160566293      -0.11442847517373124j    ,
        1.120437026895484     +0.10657570872759686j    ,
        0.7185555091427125    +0.5437834624774696j     ,
       -0.21575751536380283   +0.9977966029104395j     ,
       -0.5322899097740232    +1.1867010786414345j     ,
       -0.061921780180314356  +1.07024052597418j       ,
        0.7509004854696455    +0.6796890326273411j     ,
        0.924039594009708     -0.043513436057377175j   ,
       -0.19937437371196645   -0.5345498978639434j     ,
       -1.0722878285823731    -0.19868000064980404j    ,
       -0.14636559985410752   +0.16215825781876017j    ,
        1.059112540484913     +0.09905132262159055j    ,
        0.816316455094305     +0.42176105649432993j    ,
       -0.08339634540961643   +0.8665742627223951j     ,
       -0.6435805097245059    +0.412881137617624j      ,
       -0.9785764651674747    -0.1334337402535659j     ,
       -0.8310139505050123    +0.4182840560459963j     ,
        0.004290445128051268  +1.0134298969007245j     ,
        0.7128406615463778    +0.5201191333096475j     ,
        1.0195309584714138    -0.10288441664993914j    ,
        1.3259380805164098    -0.02954434553632075j    ,
        1.1011837857215943    +0.08874757506278119j    ,
       -0.19034166507212322   -0.1536319706405439j     ,
       -1.129108702146607     -0.13111155244116784j    ,
       -0.21706856399056268   +0.09679634899387038j    ,
        0.9293925242004695    +0.11377837827932849j    ,
        0.5599548229644581    +0.5767951583456601j     ,
       -0.04929110614683796   +1.0155230571151161j     ,
        0.02683914839447135   +0.1766783035795019j     ,
        0.08604468309850166   -0.9533483069606684j     ,
       -0.027596948737022745  -1.0858332543250029j     ,
        0.0026294665174452225 -0.8831455529685901j     ,
        0.174700783827141     -1.0596537094542597j     ,
        0.18098015489259967   -0.9479252773862955j     ,
       -0.09399722496254574   +0.017014632442037585j   ,
       -0.08200435567377806   +1.0036933858537345j     ,
        0.6250717542921815    +0.9281928768901633j     ,
        1.006251828027999     +0.2504367015618858j     ,
        0.27997145948844915   +0.3399197165602183j     ,
       -0.21816600399271474   +0.76210139427085j       ,
        0.16234234521950908   -0.013929187361872607j   ,
        0.11756520267495368   -1.0435591778152449j     ,
       -0.5372115709818335    -0.6829464047307646j     ,
       -0.8905857117898752    +0.07260600405867879j    ,
       -0.9749871659151167    -0.014727477849688364j   ,
       -1.0563425318789152    -0.08867173121227392j    ,
       -0.770436743842446     +0.6030462091824088j     ,
       -0.3005535224347538    +0.9569076805906425j     ,
       -0.5691598685153784    +0.3127113493138721j     ,
       -0.9679206395115385    -0.16761145075212505j    ,
       -0.1109594827396469    -0.01290642977546569j    ,
        0.8929952840164079    +0.2107730946665848j     ,
        0.5471766209573696    +0.6737461231316567j     ,
       -0.020167239159181005  +0.9542917380123199j     ,
        0.17651431443925633   +0.07279795986093009j    ,
        0.2713102356915082    -1.0086095133339659j     ,
       -0.19722270004647202   -0.8578063524091841j     ,
       -0.7120289213078849    -0.21288484552965437j    ,
       -1.0443834353777466    -0.2237900718523524j     ,
       -1.11222794234401      -0.1796060975316766j     ,
       -0.6551840289977229    +0.5224301746035678j     ,
       -0.2653174361554165    +0.845268492190013j      ,
       -0.6033424460779299    +0.3407339590889578j     ,
       -0.8423955369919791    -0.16360048619354j       ,
       -0.20591368622240058   -0.18016801918892905j    ,
        0.7906788060568096    -0.009691149607551214j   ,
        1.295544891230963     -0.02660639772925924j    ,
        0.9461208989283257    +0.11325995657486276j    ,
        0.19280434636772237   +0.7422541491023664j     ,
       -0.17051568366398995   +1.1033124230516833j     ,
        0.016020661643038087  +0.43284766853591544j    ,
        0.1258797507506709    -0.6924972195797864j     ,
        0.001724773428564641  -1.1145443354679314j     ,
        0.18501044384492804   -0.7494339074956119j     ,
        0.5504850449975865    -0.15921477182389984j    ,
        0.7706463255455493    +0.19742076460529845j    ,
        0.72728028100398      -0.24975491939634642j    ,
        0.15357945432426695   -0.8854546394784892j     ,
       -0.5368315224765374    -0.6421924298218692j     ,
       -0.9436810055186442    -0.17424230460084303j    ,
       -1.1845453430634376    -0.20035943357157265j    ,
       -0.8465259755236475    -0.18012662884187305j    ,
        0.16900873290833174   +0.06662673086360019j    ,
        0.7908510640773347    +0.008748599854081163j   ,
        0.2432031254159218    -0.3574045850694861j     ,
       -0.7693528791195445    -0.25261073095388964j    ,
       -0.9940316677969155    +0.5039413690956883j     ,
       -0.26848409191090933   +1.0398177391386316j     ,
        0.6288476369154249    +0.7733615830066641j     ,
        1.0399788224749658    -0.006110725023218577j   ,
        0.7434682653962884    -0.6910817810928633j     ,
       -0.03490308910381737   -0.9239929452749971j     ,
       -0.8423812208726249    -0.6303344219242357j     ,
       -1.0096403028024228    +0.0011807125846193811j  ,
       -0.21007646095699234   +0.2929902001167329j     ,
        0.7401019391699987    +0.11722747965641703j    ,
        1.0348052404089394    +0.13252608540830693j    ,
        0.988695180655101     +0.039961165771971896j   ,
        0.763474244203165     -0.7531076768777174j     ,
        0.06643373158333793   -0.963489143127306j      ,
       -0.42753115787538815   +0.311076770228074j      ,
       -0.1276669039588831    +1.131049922968124j      ,
        0.167865335781591     +0.19343857474583256j    ,
        0.11258176729089014   -0.9384908425528609j     ,
        0.21407044004047432   -1.153163021430448j      ,
        0.0958274076667       -1.0110380993999915j     ,
       -0.6081920308624695    -0.7291140556130329j     ,
       -0.8915251089860083    -0.3155381531179265j     ,
       -0.253145563221226     -0.41491284472526463j    ,
        0.010745250606436219  -0.9601745076955144j     ,
       -0.6600216325988899    -0.9040395522840808j     ,
       -0.8466098514206355    -0.22641196823922005j    ,
        0.11674640171746539   +0.09758563818941544j    ,
        0.8242589137674079    +0.05237121301226816j    ,
        0.4470515304312367    +0.4294693178683514j     ])

    expected_frame = np.array([
       -0.00001940952177043791-0.000015698909952685536j,
        0.00045504183194606325-0.00013286298404358807j ,
       -0.00042450747486277374-0.00025437545501390973j ,
        0.0001923909288544504 +0.0004612717592110326j  ,
        0.0004005235264655796 -0.001320053414637717j   ,
       -0.000625509460606032  +0.0013039078636736998j  ,
        0.00040399244697894967-0.0024597026677076164j  ,
       -0.0021938812853893024 +0.002004492181584175j   ,
        0.013938691402720292  +0.00903945317080884j    ,
       -0.013672972206868894  -0.021574189536444414j   ,
       -0.12415260099589616   -0.006962035331842773j   ,
       -0.17059351091383776   +0.095992137724738j      ,
       -0.057961470980332636  +0.12195256751120961j    ,
        0.03645908139392493   +0.0025501761086182497j  ,
       -0.013752942901524644  -0.0558504234465463j     ,
       -0.08842246328469827   -0.027707356161776314j   ,
       -0.13227926346390084   -0.06392597850840492j    ,
       -0.11058394394716732   -0.06467796805683831j    ,
       -0.06279997424029128   +0.13885449697471877j    ,
       -0.1291076606205923    +0.707130472006586j      ,
       -0.15120667275261254   +1.420781425662896j      ,
       -0.03362229590381882   +1.6826816966269362j     ,
        0.08738753809080135   +1.4841177101967205j     ,
        0.07279825299317902   +1.2853521505681407j     ,
       -0.06901752329430136   +1.3601616257851836j     ,
       -0.10462021078009477   +1.426522043891903j      ,
       -0.37483070322119666   +1.5008336932095818j     ,
       -0.6216000979261183    +1.950800894163329j      ,
       -0.24478520633756762   +1.6221691119125512j     ,
        0.10162015965575538   -0.034473836015486106j   ,
        0.34218812503673157   -1.606351459620057j      ,
        0.6467763094784384    -2.3223686026317405j     ,
        0.36479934641541645   -1.890446283438096j      ,
       -0.1819607398419365    -0.3846726963986691j     ,
       -0.4268114307848103    +1.2619498360994652j     ,
       -0.3050618986693503    +2.269329397060908j      ,
        0.17045694537401693   +1.8333140960325425j     ,
        0.5517004006338371    -0.0721745027701167j     ,
        0.18845164160559438   -1.3182349135635585j     ,
       -0.7560655649324566    -0.13476054103889654j    ,
       -0.7104329784590824    +1.3353509776002044j     ,
        0.35009066338811484   +0.20669847930614269j    ,
        0.5854444168383153    -1.4662800776897578j     ,
       -0.21360017646463864   -0.5050905604654803j     ,
       -0.28419659346087467   +1.6305774562493887j     ,
        0.8050879300878254    +2.000491910344557j      ,
        1.5866586035230548    +0.5509828358574167j     ,
        1.208638842458495     -1.0644868634973585j     ,
        0.7721845820228046    -1.6361977050979393j     ,
        1.2194141898467004    -0.8868597714486423j     ,
        1.483574758770675     +0.3453314184181189j     ,
        0.680804310027458     +1.1704885072896554j     ,
       -0.3227624094780427    +1.5196227383351397j     ,
       -0.5849819112678465    +1.6628415068640967j     ,
       -0.5203483742655325    +1.4256996305138445j     ,
       -0.8980424091460095    +0.6212698719420405j     ,
       -1.2812508712216308    -0.4322066772307866j     ,
       -0.9036045167777809    -1.2401809785284037j     ,
        0.08637036831056366   -1.3617583369664485j     ,
        0.9591243117431674    -0.6166792696233876j     ,
        1.2708891023726876    +0.3487245363298392j     ,
        0.7508702612686348    +0.6954232872084282j     ,
       -0.2596206430834367    +0.9248987288683215j     ,
       -0.5641031609198606    +1.4957168691660492j     ,
       -0.27304967750129977   +1.3296302417031036j     ,
       -0.6571089514571343    +0.3307635208526583j     ,
       -1.2796326527794408    -0.2855315099040194j     ,
       -1.2813179263549683    -0.3215607929598997j     ,
       -1.2413292077996712    -0.2090333931424108j     ,
       -1.4698189815390013    -0.1288654404173116j     ,
       -1.2313850505320592    -0.3126651076969787j     ,
       -0.28231671312744056   -0.8305435856834644j     ,
        0.6583679180265688    -1.1240965050619718j     ,
        1.0452494404037687    -0.6256493399603615j     ,
        0.9431325017946738    +0.3699124932201121j     ,
        0.3977407220978401    +1.1083634937088185j     ,
       -0.3383606067751414    +1.2095283531133063j     ,
       -0.8351694853191955    +0.6043129567855701j     ,
       -1.090865137563974     -0.18553361614765537j    ,
       -1.0968707112636673    -0.5095513414350292j     ,
       -0.9125888297669265    -0.2579089070882565j     ,
       -0.6870468413289487    +0.4679060069778932j     ,
       -0.5427888962433844    +0.8160576777744473j     ,
       -0.8650234690344715    +0.15384775131723358j    ,
       -0.9148867707313975    -0.37291083392089225j    ,
        0.16527810321252356   -0.06901848390267673j    ,
        1.0419591725581474    +0.42550980676257244j    ,
        0.5271010688912767    +0.730880932133957j      ,
       -0.4996044644966106    +0.8902498218312822j     ,
       -0.8634452675934421    +0.972653210536248j      ,
       -0.3792311238741197    +1.0027127430043765j     ,
        0.5095885728034772    +0.8752989241513754j     ,
        0.89330801971181      +0.24029850672384584j    ,
       -0.023484007423529407  -0.5700370475633341j     ,
       -0.9584892727107827    -0.5201665541751622j     ,
       -0.18997057480386775   +0.10783955725129954j    ,
        0.9754643008671755    +0.42426399288556826j    ,
        0.6411923052319689    +0.6581241306503353j     ,
       -0.35332932155077024   +0.7956533753922088j     ,
       -0.7421721255188325    +0.18397620063621367j    ,
       -0.8832546773550578    -0.44190229253550906j    ,
       -0.9220881210766352    +0.12369007415956135j    ,
       -0.3240207837630871    +0.9602442895123953j     ,
        0.5027551960702743    +0.7251916535737271j     ,
        0.9980788404934354    +0.23209309905793735j    ,
        1.261875547583271     +0.40823371263056j       ,
        1.0110102417660742    +0.4453539637858521j     ,
       -0.12786495400871103   -0.20852646211374587j    ,
       -1.015935859823508     -0.5098539292497393j     ,
       -0.23718132918326196   +0.0152745454377302j     ,
        0.8316025848152715    +0.4302942299545201j     ,
        0.32025104173792085   +0.7373474952272701j     ,
       -0.40412010687804145   +0.9329542496256129j     ,
       -0.03792560109622795   +0.17463450868531363j    ,
        0.4185179593186864    -0.8608829186376141j     ,
        0.3647219547529664    -1.0231194180049539j     ,
        0.3219048571785903    -0.8223929989653331j     ,
        0.5505013130806959    -0.9221359184666975j     ,
        0.5206616873031835    -0.8125438790289646j     ,
       -0.09347909959127466   -0.019663009876456427j   ,
       -0.45795712754320966   +0.8968837140278427j     ,
        0.22070761169041792   +1.0970619238973955j     ,
        0.8317869124754762    +0.6191864138798601j     ,
        0.12519537173970635   +0.42220321023107843j    ,
       -0.4946745918811575    +0.6194287599029714j     ,
        0.15505167269056555   +0.050080316570386654j   ,
        0.5118405600906168    -0.9169823201831955j     ,
       -0.22956373063505053   -0.8380409043169461j     ,
       -0.8482115871370564    -0.2809833541619208j     ,
       -0.8900339915792539    -0.3983169167089255j     ,
       -0.9373618165733703    -0.495050548330986j      ,
       -0.9464416034480193    +0.2479632995718652j     ,
       -0.6593784033293777    +0.7557941851086852j     ,
       -0.6470869432919253    +0.05486193342617385j    ,
       -0.8189422258785427    -0.5424920215899545j     ,
       -0.09630114662724065   -0.05660982156549975j    ,
        0.7337405947903117    +0.550899822352153j      ,
        0.2285156078201453    +0.8373271224198174j     ,
       -0.4051699062329932    +0.8642434760280376j     ,
        0.13149267427907554   +0.13844321136412285j    ,
        0.6561103042605401    -0.8126633146770577j     ,
        0.17083971071171028   -0.8634479283032123j     ,
       -0.5621075321385613    -0.48614839766078743j    ,
       -0.8591710395457832    -0.6345422611275967j     ,
       -0.9349765619851442    -0.6285922164168024j     ,
       -0.8140655419484312    +0.19873774830718582j    ,
       -0.5979712991648938    +0.6536837853215502j     ,
       -0.6910326132485475    +0.05094767455555499j    ,
       -0.6940170260082924    -0.5047135102584165j     ,
       -0.10988885684317377   -0.2505701507639328j     ,
        0.7211505101895764    +0.32435911330106254j    ,
        1.1846886661699658    +0.5250306941914946j     ,
        0.8088350362069932    +0.5037444365512289j     ,
       -0.14344189102600333   +0.7533519507752315j     ,
       -0.6323383466364034    +0.9200663653284551j     ,
       -0.17484874662628294   +0.39628484901605354j    ,
        0.41947530392228016   -0.5651889773996805j     ,
        0.4986241234321424    -0.9967878581215566j     ,
        0.5016564087747191    -0.5867034119306711j     ,
        0.5631257558246586    +0.10617208418335913j    ,
        0.5959928339485222    +0.5269376236863399j     ,
        0.760960121995867     +0.11069697209923443j    ,
        0.5452814221176254    -0.7143421715521918j     ,
       -0.17783048153827302   -0.8179092371900805j     ,
       -0.7514016633808583    -0.5969001266189944j     ,
       -0.9497841203837629    -0.7356641197321236j     ,
       -0.6633478435869381    -0.5558969941120029j     ,
        0.11770142590161489   +0.13838152841176848j    ,
        0.6923176017867152    +0.3823849916091774j     ,
        0.38395461821641863   -0.1986571136180335j     ,
       -0.5557818142605889    -0.58891647025686j       ,
       -1.113914028347641     -0.03537509744841838j    ,
       -0.734849249611869     +0.7831355046104562j     ,
        0.17906212279544786   +0.9805479308553333j     ,
        0.9096015094564086    +0.5042007399353445j     ,
        0.987147540876347     -0.2363870181537701j     ,
        0.4197692692144122    -0.8238779941048013j     ,
       -0.4239917155089879    -0.9628907673880565j     ,
       -0.8821655843750311    -0.49107923685433397j    ,
       -0.32694430296881205   +0.15193024573433545j    ,
        0.5882700144246453    +0.46414604649680646j    ,
        0.8350488982682003    +0.6253626039287268j     ,
        0.8405309030941203    +0.5221329868570462j     ,
        1.0361742140915207    -0.2764183289609533j     ,
        0.537153537536467     -0.80261500529727j       ,
       -0.5258631594629313    +0.05495075476700678j    ,
       -0.6730973130937828    +0.9178849457958093j     ,
        0.0485920354343322    +0.2514678254749779j     ,
        0.5652003044979041    -0.757620176392759j      ,
        0.7631380253990477    -0.8906354256842497j     ,
        0.5894389536079234    -0.827008252962486j      ,
       -0.15835284751859063   -0.9361779895830995j     ,
       -0.6096361660405217    -0.7229972967314606j     ,
       -0.0070164513573656995 -0.4859898294274819j     ,
        0.4935779328940213    -0.8236694542102333j     ,
       -0.11335902858080893   -1.1135824164522896j     ,
       -0.6179935510265837    -0.6213651026361082j     ,
        0.051282516907838485  +0.14325774867143684j    ,
        0.6873271170573665    +0.45795953427678815j    ,
        0.1712129956738913    +0.5958062402858753j     ])

    out_frame = np.empty_like(in_frame)
    fsync(in_frame, out_frame)
    assert np.allclose(out_frame, expected_frame)
