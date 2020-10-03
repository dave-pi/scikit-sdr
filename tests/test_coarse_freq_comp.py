import logging

import numpy as np

import sksdr

_log = logging.getLogger(__name__)

def test_coarse_freq_comp():
    mod = sksdr.QPSK
    sample_rate = 200.0e3
    resolution = 25.0

    in_frame = np.array([
       -0.00001940952177043791-0.000015698909952685536j,
        0.00047383661248221425+0.00001394654154892672j ,
       -0.00019450913096894033-0.00045506006888938267j ,
       -0.0002592569322008952 +0.0004272841542309983j  ,
        0.0013791389600119053 -0.000030591530304981574j,
       -0.001305939176882931  -0.0006212573287616764j  ,
        0.0022189311429717095 +0.001135645936678446j   ,
       -0.00034562204568971055-0.002951550338711295j   ,
       -0.016585071785405726  +0.0009665534234865577j  ,
        0.019766234995019633  +0.01617689022172982j    ,
        0.12419549962730153   +0.006149483094778765j   ,
        0.19162316652004902   -0.039964966204218424j   ,
        0.11806472893151194   -0.06551855174764386j    ,
       -0.019657543407505154  -0.030811507614134384j   ,
       -0.048577573030335344  +0.030799880455832342j   ,
       -0.02676609837378194   +0.08871192465871974j    ,
       -0.10044202468935241   +0.10721816052848816j    ,
       -0.11670601846672356   +0.05283704632657295j    ,
        0.03274935786986215   +0.14883510222321591j    ,
        0.10583777559053231   +0.7109856944617292j     ,
       -0.12955328350822296   +1.4229192753370954j     ,
       -0.5256612671651314    +1.598820935298102j      ,
       -0.7742597615315578    +1.26915869031663j       ,
       -0.9701428042898949    +0.8463171248967739j     ,
       -1.2971363281585522    +0.41501856940578274j    ,
       -1.4293594768272668    -0.0533105638432563j     ,
       -1.3332720680346888    -0.784465055530783j      ,
       -1.274607354166314     -1.6023067443892733j     ,
       -0.8260866415589336    -1.4173684367597446j     ,
       -0.08207100402849157   +0.06913358457247218j    ,
       -0.22876724707281462   +1.6263834945689677j     ,
       -1.1640065601606557    +2.1111144566070337j     ,
       -1.293525503654684     +1.4260636329087564j     ,
       -0.16865191867828133   +0.39069082984449727j    ,
        1.3261249533233812    -0.12679903175144605j    ,
        2.2895402402595777    +0.030400043037620717j   ,
        1.831713741040584     +0.18687138844929657j    ,
        0.201632495114949     -0.5185815536859849j     ,
       -0.7848614600192125    -1.0757554541522325j     ,
       -0.7402135867238501    +0.20464454042838345j    ,
       -0.532423975612195     +1.4157690349959522j     ,
        0.30876801926320163   +0.2644807067051987j     ,
        1.1995911963733712    -1.0265005567560794j     ,
        0.20907818366343836   -0.506979114730632j      ,
       -1.5836126618232922    +0.4813745754362591j     ,
       -1.8449070485670804    +1.1164463447361084j     ,
       -0.7874335516475386    +1.4835821552185622j     ,
        0.42333373478486686   +1.5539397295426074j     ,
        0.6226527544155169    +1.6987393873988634j     ,
       -0.6619985113357297    +1.3547136935909j        ,
       -1.5209025765788842    -0.08428051948017642j    ,
       -0.5198098162585012    -1.250334198992586j      ,
        0.9496430808651335    -1.2294742204707823j     ,
        1.5634105530819336    -0.8142439167550988j     ,
        1.5002649672272905    -0.22931832713194145j    ,
        0.7858976857370692    +0.7581696709581351j     ,
       -0.5656302385592475    +1.2281973945895155j     ,
       -1.4982311917480018    +0.3314412139704989j     ,
       -0.9600768530321497    -0.9695865330601562j     ,
        0.507972933833029     -1.0208703470338947j     ,
        1.3164937456819032    +0.060101001227505745j   ,
        0.6924626057734333    +0.7536015109159949j     ,
       -0.5963488955948433    +0.753132479514796j      ,
       -1.3962602342366397    +0.7783564011152677j     ,
       -1.2730606976022918    +0.470944971578829j      ,
       -0.48268780184960774   -0.5551658912050841j     ,
        0.356766652695073     -1.2616281245803658j     ,
        0.7527817152102345    -1.0855858608201991j     ,
        0.9394801112669134    -0.8378366679246603j     ,
        1.2928464421502204    -0.7110008560091976j     ,
        1.269613265255832     -0.046376383337100785j   ,
        0.2662259319696689    +0.8358403719478432j     ,
       -0.9796843582882706    +0.8586383559476466j     ,
       -1.213553472788507     -0.10616712268957083j    ,
       -0.25409362454889317   -0.9806990356604853j     ,
        0.9281250179453525    -0.7247422074539802j     ,
        1.210392755880332     +0.3352552963260146j     ,
        0.32517990351783793   +0.9782434509340596j     ,
       -0.787643655945778     +0.7771917024271826j     ,
       -1.1837226918125598    +0.248130037831636j      ,
       -0.9470644226714772    +0.049034231724058346j   ,
       -0.6766953474157584    +0.48275542496376767j    ,
       -0.7510215255350596    +0.6297115113468443j     ,
       -0.8031694354514141    -0.3561651169365936j     ,
       -0.26936626659797713   -0.9505377992136701j     ,
        0.12188464715909188   +0.1312422771391037j     ,
       -0.389022171954286     +1.0561246435232685j     ,
       -0.8460646148584821    +0.3101566398897445j     ,
       -0.4648189668689719    -0.9088964155801453j     ,
        0.06430459071337896   -1.2990215231893452j     ,
       -0.0009448652155712375 -1.072029942458658j      ,
       -0.5553122363024222    -0.8470283586546811j     ,
       -0.8021969620116807    -0.4606762687119618j     ,
       -0.2858792818596467    +0.4937274252082861j     ,
        0.2083492632444329    +1.0704510799142617j     ,
        0.1709066296583406    +0.13604820226043055j    ,
        0.359575743344289     -1.0011172871966076j     ,
        0.793320489605265     -0.4635704309006434j     ,
        0.4888799598909319    +0.7203487266994948j     ,
       -0.44533187047688666   +0.6215675598317818j     ,
       -0.9851905316700824    -0.0693979648501749j     ,
       -0.9083267384289835    +0.20121698171675795j    ,
       -0.5362512455432429    +0.8599378846782659j     ,
        0.05742593349171185   +0.8805498190058652j     ,
        0.47549114909502643   +0.9077096152423028j     ,
        0.12016990378385457   +1.3208118170054695j     ,
       -0.35325235654402315   +1.0467543334573592j     ,
        0.23115744681534442   -0.07999354128388424j    ,
        0.9488511142105647    -0.625905954204063j      ,
        0.16478821793377568   -0.1712691971186839j     ,
       -0.9351561547197783    -0.04689295995469136j    ,
       -0.4055553007118981    -0.6940943426628937j     ,
        0.5772675887460971    -0.8369461294855705j     ,
        0.11757345717020316   -0.13458099795780046j    ,
       -0.9149024029140067    +0.28147872924338496j    ,
       -1.0807158537836783    +0.10885169341004929j    ,
       -0.8575183537842294    -0.21122323438852214j    ,
       -0.8106305531768156    -0.7044603992320929j     ,
       -0.4766589066886505    -0.8391140772548241j     ,
       -0.08038041517690027   +0.05161361132284983j    ,
       -0.0033116419781999687 +1.0070323530966685j     ,
        0.391480498617588     +1.048331881574565j      ,
        0.7278546896778717    +0.7385721587040875j     ,
       -0.07593485330584249   +0.4337779730321627j     ,
       -0.7873690286047726    +0.09189642670800349j    ,
        0.02709804305882635   +0.1606697089507366j     ,
        0.9885643745240922    +0.3543695978836545j     ,
        0.8625611630735076    -0.10488233258621171j    ,
        0.6269351094530506    -0.6366843098465197j     ,
        0.9043935530854091    -0.3645396733423587j     ,
        1.060057112645154     -0.0010670065410088476j  ,
        0.8871162662154015    -0.4126284489560423j     ,
        0.7512732594357533    -0.6645248066687054j     ,
        0.6092833708964931    +0.22473343735891155j    ,
        0.22399923118139045   +0.9564456635093306j     ,
       -0.003103295124200153  +0.11166446300757972j    ,
        0.4051010085283222    -0.8232612268291338j     ,
        0.8590780522500381    -0.12377799925488915j    ,
        0.6128304777518911    +0.7317911206842201j     ,
        0.19091907000492211   -0.0025990133377661708j  ,
        0.17825103681033588   -1.0291399138381532j     ,
       -0.00330276881810887   -0.8801804493200835j     ,
       -0.5035928921434853    -0.5465339341867208j     ,
       -0.5218453586155088    -0.931931423465566j      ,
       -0.2764825795753777    -1.0921843842468604j     ,
       -0.58194100625538      -0.6029461538383665j     ,
       -0.767448973055693     -0.44259941207939246j    ,
        0.012742347272252756  -0.6927910007366785j     ,
        0.7391064898081598    -0.4360240320787697j     ,
        0.26077214979400587   +0.08281815745337565j    ,
       -0.7859549344471438    +0.08684315601314671j    ,
       -1.2712135532223863    -0.25131766292580976j    ,
       -0.7595102390761814    -0.5754274670979174j     ,
        0.4257680359073653    -0.6378372186048311j     ,
        1.0785368682628136    -0.28832642097701855j    ,
        0.42902342958788076   -0.05960421647091068j    ,
       -0.6503838430690578    -0.2690705622127941j     ,
       -0.9630372078328395    -0.5610449063101466j     ,
       -0.36281301733983534   -0.6813565589943367j     ,
        0.4385262679675026    -0.3688873007239819j     ,
        0.787013304525114     +0.11610674345040306j    ,
        0.7632917979702194    -0.09327249354066475j    ,
        0.5751133383557139    -0.6905513850611461j     ,
        0.11674970593385874   -0.8288357536987355j     ,
       -0.22670215200111488   -0.9324700290987136j     ,
        0.07202491213802453   -1.199209733293517j      ,
        0.349421855618924     -0.7918056557451638j     ,
       -0.1417339019579476    +0.11364230770547262j    ,
       -0.5910517321848939    +0.5255281090797103j     ,
       -0.07448429071770786   +0.42583786595022766j    ,
        0.7925722074563115    +0.16596785824496368j    ,
        1.07512461735667      -0.29353520610452927j    ,
        0.7467210007841615    -0.7718240636469565j     ,
        0.14598992149929657   -0.9860144174125025j     ,
       -0.43682467005128245   -0.9438100973137096j     ,
       -0.7712271957745586    -0.6599603793467915j     ,
       -0.9125956251997321    -0.1488301495439105j     ,
       -0.9625984076035953    +0.42465504874007715j    ,
       -0.7418095099553118    +0.6849040707026318j     ,
       -0.06850998838275026   +0.35395163271901053j    ,
        0.7487368829725497    +0.02976982408981493j    ,
        0.9891308063977088    +0.33167046405501793j    ,
        0.8435434230518792    +0.5172519197126251j     ,
        1.071343530598782     +0.04782398956468729j    ,
        0.9020604262641511    -0.34498080668990155j    ,
       -0.3602562434944288    -0.38699752835526335j    ,
       -1.0855978348489645    -0.34212586511967535j    ,
       -0.2505816965555876    +0.0529723183189934j     ,
        0.5580112482003747    +0.7629306408604775j     ,
        0.2945193950793836    +1.1352838557892895j     ,
        0.02982302882788831   +1.0151312808942485j     ,
        0.45984790338687825   +0.8306893271541366j     ,
        0.6288911093016628    +0.7063124794783894j     ,
       -0.12909291213548085   +0.46858335964157355j    ,
       -0.8730422141580361    +0.39980975217839865j    ,
       -0.8130621481062794    +0.7693152870633131j     ,
       -0.3793689757952459    +0.7899935443334295j     ,
        0.14160431304105883   -0.05568570393719666j    ,
        0.6349061712674899    -0.5282420416474443j     ,
        0.588166004200547     +0.19585636919431573j    ])

    expected_frame = np.array([
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

    cfc = sksdr.CoarseFrequencyComp(mod.order, sample_rate, resolution)
    out_frame, _, _ = cfc(in_frame)
    assert np.allclose(out_frame, expected_frame)