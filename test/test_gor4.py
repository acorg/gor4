from unittest import TestCase

from gor4.gor4 import GOR4


class TestGOR4(TestCase):
    """
    Tests for the L{dark.gor4.GOR4} class.
    """

    def testApoamicyanin(self):
        """
        Test the GOR IV secondary structure prediction a fragment of the
        APOAMICYANIN sequence from the GOR IV reference database.
        """
        gor4 = GOR4()
        seq = 'DKATIPSESPFAAAEVADGAIVVDIAKMKYETPELHVKVGDTVTWINREA'
        result = gor4.predict(seq)

        expected = 'CCCCCCCCCCHHHHHHHCCHHHHHHHHHCCCCCCEEEEECCCEEECCCCC'
        self.assertEqual(expected, result['predictions'])

        # Below are the probabilities we get from running the command-line
        # version of the GOR IV code.
        expected = (
            (4.712939816187145e-09, 0.0003676836786326021, 0.9996322989463806),
            (9.411732548869622e-08, 0.0002178027352783829, 0.9997820854187012),
            (6.726327228534501e-07, 0.0015486916527152061, 0.9984506368637085),
            (7.0672699621354695e-06, 0.005548186134546995, 0.994444727897644),
            (0.0001701521105132997, 0.012098101899027824, 0.9877317547798157),
            (0.0018776297802105546, 0.01288850512355566, 0.9852338433265686),
            (0.00901438295841217, 0.02868419699370861, 0.9623014330863953),
            (0.04382030665874481, 0.04231758415699005, 0.9138621091842651),
            (0.12408247590065002, 0.03347907215356827, 0.8424384593963623),
            (0.39440542459487915, 0.03329133614897728, 0.5723032355308533),
            (0.521320104598999, 0.08230321854352951, 0.39637666940689087),
            (0.5871812105178833, 0.10948990285396576, 0.30332887172698975),
            (0.7104831337928772, 0.10078689455986023, 0.18872997164726257),
            (0.7383258938789368, 0.11010399460792542, 0.15157009661197662),
            (0.6967296600341797, 0.13061337172985077, 0.17265696823596954),
            (0.6338369250297546, 0.11982367187738419, 0.24633941054344177),
            (0.5137858390808105, 0.07652368396520615, 0.4096904695034027),
            (0.33978256583213806, 0.043581265956163406, 0.6166361570358276),
            (0.37997493147850037, 0.07173365354537964, 0.5482913851737976),
            (0.4227449893951416, 0.18985646963119507, 0.38739854097366333),
            (0.3843967616558075, 0.45084795355796814, 0.16475528478622437),
            (0.36887481808662415, 0.5519948601722717, 0.07913032174110413),
            (0.4489874243736267, 0.47397562861442566, 0.07703694701194763),
            (0.48342230916023254, 0.38773414492607117, 0.1288435310125351),
            (0.5846329927444458, 0.26836836338043213, 0.14699867367744446),
            (0.5704081654548645, 0.20060157775878906, 0.22899024188518524),
            (0.5412087440490723, 0.12875805795192719, 0.33003315329551697),
            (0.4612639248371124, 0.10551358014345169, 0.4332224726676941),
            (0.3290359079837799, 0.12168093770742416, 0.5492831468582153),
            (0.2980051338672638, 0.12314165383577347, 0.578853189945221),
            (0.1978907287120819, 0.10649622231721878, 0.6956130266189575),
            (0.10552268475294113, 0.08139842003583908, 0.8130788803100586),
            (0.2553287148475647, 0.07425926625728607, 0.670412003993988),
            (0.25931549072265625, 0.23121821880340576, 0.509466290473938),
            (0.20519335567951202, 0.41565483808517456, 0.3791518211364746),
            (0.13479138910770416, 0.5870223641395569, 0.27818629145622253),
            (0.09040924906730652, 0.7083150744438171, 0.20127567648887634),
            (0.093185193836689, 0.6218422651290894, 0.28497254848480225),
            (0.0848071351647377, 0.4761156141757965, 0.4390772581100464),
            (0.06407877802848816, 0.237196683883667, 0.6987245678901672),
            (0.07805037498474121, 0.2266431748867035, 0.6953064799308777),
            (0.13069340586662292, 0.42894041538238525, 0.4403661787509918),
            (0.11789494007825851, 0.5780963897705078, 0.3040086627006531),
            (0.07004909962415695, 0.6333698630332947, 0.2965810298919678),
            (0.05527617037296295, 0.600002110004425, 0.3447217047214508),
            (0.03358002379536629, 0.3309133052825928, 0.6355066895484924),
            (0.007320968434214592, 0.07492919266223907, 0.91774982213974),
            (0.0011769048869609833, 0.013734811916947365, 0.9850882887840271),
            (0.0001740210864227265, 0.0013027909444645047, 0.9985231757164001),
            (5.1828601499437355e-06, 0.12864187359809875, 0.8713529109954834))
        for e, r in zip(expected, result['probabilities']):
            self.assertAlmostEqual(e[0], r[0])
            self.assertAlmostEqual(e[1], r[1])
            self.assertAlmostEqual(e[2], r[2])

    def testAldoseReductase(self):
        """
        Test a fragment of the ALDOSE REDUCTASE sequence from the GOR IV
        reference database.
        """
        gor4 = GOR4()
        seq = 'LDYLDLYLIHWPTGFKPGKEFFPLDESGNVVPSDTNILDTWAAMEELVDE'
        expected = 'CCCCCCCEEECCCCCCCCCEEEECCCCCCEECCCCCCHHHHHHHCCCCCC'
        result = gor4.predict(seq)
        self.assertEqual(expected, result['predictions'])

        # Below are the probabilities we get from running the command-line
        # version of the GOR IV code (with the printout function adjusted
        # to print 7 decimal places).
        expected = (
            (2.9084640118526295e-07, 0.002895076060667634, 0.9971046447753906),
            (5.2858044909953605e-06, 0.000120705168228596, 0.9998739957809448),
            (0.00026573732611723244, 0.001878385432064533, 0.9978559017181396),
            (0.0007981329108588398, 0.009710855782032013, 0.9894909858703613),
            (0.004144459031522274, 0.037500787526369095, 0.9583547711372375),
            (0.01709458790719509, 0.19731156527996063, 0.7855938673019409),
            (0.04360358044505119, 0.44768092036247253, 0.5087155103683472),
            (0.1101851835846901, 0.5581879019737244, 0.33162692189216614),
            (0.1755424588918686, 0.5546174049377441, 0.26984015107154846),
            (0.09620075672864914, 0.5103141665458679, 0.39348503947257996),
            (0.05799134075641632, 0.2558242380619049, 0.6861844062805176),
            (0.10065478086471558, 0.11877889186143875, 0.7805663347244263),
            (0.060057081282138824, 0.09369701147079468, 0.8462458848953247),
            (0.030554573982954025, 0.06951101869344711, 0.8999344110488892),
            (0.025212019681930542, 0.08770088851451874, 0.8870871067047119),
            (0.021249763667583466, 0.07142526656389236, 0.9073249697685242),
            (0.03146269544959068, 0.04803548753261566, 0.9205018281936646),
            (0.04128308594226837, 0.047556567937135696, 0.9111603498458862),
            (0.06726472079753876, 0.16425780951976776, 0.7684774994850159),
            (0.05349395051598549, 0.4758519232273102, 0.47065412998199463),
            (0.045901600271463394, 0.6615397334098816, 0.2925586700439453),
            (0.030837304890155792, 0.612140417098999, 0.3570222854614258),
            (0.06721237301826477, 0.47314730286598206, 0.4596403241157532),
            (0.09089970588684082, 0.3464865982532501, 0.5626136660575867),
            (0.0798494964838028, 0.16784276068210602, 0.7523077726364136),
            (0.0695127472281456, 0.11025030165910721, 0.8202369809150696),
            (0.039651427417993546, 0.10260476917028427, 0.8577437996864319),
            (0.022757239639759064, 0.13472241163253784, 0.8425203561782837),
            (0.016810795292258263, 0.26520636677742004, 0.717982828617096),
            (0.01959366537630558, 0.564834475517273, 0.41557183861732483),
            (0.015847401693463326, 0.5475763082504272, 0.4365762770175934),
            (0.03682711720466614, 0.3752058148384094, 0.5879670977592468),
            (0.03793191909790039, 0.2514844536781311, 0.7105836272239685),
            (0.06430027633905411, 0.15815553069114685, 0.7775442004203796),
            (0.12068060040473938, 0.15617237985134125, 0.7231470346450806),
            (0.17871740460395813, 0.19766145944595337, 0.6236211061477661),
            (0.34435537457466125, 0.2679608166217804, 0.38768380880355835),
            (0.5243793725967407, 0.2100689560174942, 0.2655516564846039),
            (0.6118974685668945, 0.12235391139984131, 0.2657485902309418),
            (0.7334406971931458, 0.0865916758775711, 0.17996762692928314),
            (0.8175395131111145, 0.06751289963722229, 0.11494758725166321),
            (0.8311835527420044, 0.050035860389471054, 0.11878059804439545),
            (0.7342361807823181, 0.047467075288295746, 0.21829673647880554),
            (0.6476150751113892, 0.04069047421216965, 0.3116944432258606),
            (0.40908175706863403, 0.04099256545305252, 0.549925684928894),
            (0.14668050408363342, 0.03940052166581154, 0.8139190077781677),
            (0.025901097804307938, 0.016506606712937355, 0.9575923085212708),
            (0.0026051511522382498, 0.002299227984622121, 0.9950956106185913),
            (0.0001605961006134748, 0.00017782370559871197, 0.999661564826965),
            (4.1104763113253284e-06, 0.02834026888012886, 0.9716556072235107))

        for e, r in zip(expected, result['probabilities']):
            self.assertAlmostEqual(e[0], r[0])
            self.assertAlmostEqual(e[1], r[1])
            self.assertAlmostEqual(e[2], r[2])