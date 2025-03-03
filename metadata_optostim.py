pids_list_STN_ipsi = ['c547dda9-2006-4e4d-9498-396aac25d54b','c4051389-6e82-4c48-9116-fc5be6ebace9','60668d72-b4ba-4c59-830a-915458f62192', #24 17/2, 16/2, 15/2
                      '6ee63cc8-37ef-49ff-8c00-70a03e503725','126cfd2e-2fa4-4d81-a520-25bbeab59fae','6bfade8f-e22a-42fa-b8d0-8c22d172c237', #25 9/12, 8/12, 7/12
                      '442a8e82-4be2-4fdf-b457-6d7f4b0111e5','bc5d45e1-7e63-4d32-94f2-f785be9e75f8'] #26 16/2, 15/2

pids_list_STN_contra = ['19b9e2f8-5e46-4ff4-bef3-4652019be01a','d082c08d-2c7e-4761-9936-8bbefa8068d1','ae535cc1-87aa-4fa8-acca-8892c8f81e4c', #24 17/2, 16/2, 15/2
                        '6509394a-ee93-4164-a516-d4d483fb5da0','1bffcd91-1e56-4724-9047-69e18bc7a104', #25 8/12, 7/12
                        '855ef2f9-4a68-4398-bf3d-c9a6b7c44702','dcd1c7d3-b413-47dc-a120-c3cafbbbbd96'] #26 16/2, 15/2

pids_list_ZI_directstim = ['c2f05bd0-bd6e-4d9c-8c34-aeb086f77045', '1285d34a-d2a2-418b-9ba7-b0ad55025b6c', #SWC_NM_023 25/8/22, #SWC_NM_023 26/8/22 #this second penetration is shit
                           'ccfb329e-c3b0-43be-9710-5d7c8ee968d2', #SWC_NM_020 23/3/22
                           'e44cb3ae-d436-4149-9110-415a276fb58e','bfa8f605-2eda-4b31-80fb-4a889fa0e22a', #SWC_NM_028 28/9, #SWC_NM_028 29/9 need to manually check each trial for stim...
                           '521e3ea4-8371-4255-939d-94c27562e8cf','40326941-93ee-4aa0-9609-b7ec52241a0f', #SWC_NM_032 16/1, 17/1
                           'ae8674d7-c682-4f6e-a79c-a695f2f0b13b'] #SWC_NM_032 18/1
pids_list_SNr_directstim = ['e91b783b-ec23-4963-9cc0-601c4d093d0f', '9fedd1c6-33eb-48b6-b508-8deebe3ee44c', #SWC_NM_021 SNr 23/3/22, #SWC_NM_027 8/9/22 003
                            # '216e8284-66ea-4e2b-8033-417fea3e9f71'] #SWC_NM_027 7/9/22
                            '11f2f5b2-d542-4b58-9759-036e723c1d65'] #SWC_NM_030
excitation_trials_range_list_SNr_directstim = [list(range(54,138)) + list(range(193,276)) + list(range(358,403)), #SWC_NM_021 SNr 23/3/22
                                               list(range(18,49)) + list(range(89,112)) + list(range(135,159)), #SWC_NM_027 8/9/22 003
                                            #    list(range(1,56)) + list(range(136,220))] #SWC_NM_027 7/9/22
                                               list(range(208,335))] #SWC_NM_030
inhibition_trials_range_list_SNr_directstim = [list(range(0,54)) + list(range(140,193)) + list(range(276,358)), #SWC_NM_021 SNr 23/3/22
                                               list(range(0,18)) + list(range(49,89)) + list(range(112,135)), #SWC_NM_027 8/9/22 003
                                               #list(range(56,136)) + list(range(220,275))]
                                               list(range(101,208)) + list(range(335,364))] #SWC_NM_030

light_artifact_units_SNr_directstim = [[1,4,5,10,11,38,59,162,173,175,206,218],
                                       [8,16,28,52,53,98,102,103,114,116]]
                                    #    []]

### not correct? use other metadata file to see correct eids
pids_list_SNr = ['518b61c2-45bc-40c2-bee1-d87b0d1986ac','e4696ffd-248e-41cb-a62a-16e320b8cd7e', #SWC_NM_018 15/6, SWC_NM_018 16/6
                 '59bf32ee-1d83-4a7f-bf14-590b610c96e0', #SWC_NM_018 17/6 (few trials)
                 '0d60096b-a037-4b6f-a50c-ff469298ba71', #SWC_NM_012
                 'f080b240-b025-4aa4-b0c3-74809c0cc3db','464b7b30-7456-483b-8e57-e3dbc918079d', #SWC_NM_021 22/3/22, 24/3 (goes through IC, very little modulation)
                 '503cccbe-da42-4451-b97c-34e1726595d7', 'dc1dc606-699e-48ac-ab9d-53b202d77b66',# SWC_NM_016 ###for this mouse, only L hemi stim gives stereotypes behaviour effect...
                 'e91b783b-ec23-4963-9cc0-601c4d093d0f'] #SWC_NM_021 SNr 23/3/22
                 # SWC_NM_027! (7/9 and 8/9) need to manually check each trial for stim...
pids_list_SNr_trained = ['518b61c2-45bc-40c2-bee1-d87b0d1986ac','e4696ffd-248e-41cb-a62a-16e320b8cd7e', #SWC_NM_018 15/6, SWC_NM_018 16/6
                         '59bf32ee-1d83-4a7f-bf14-590b610c96e0', #SWC_NM_018 17/6 (few trials)
                         '0d60096b-a037-4b6f-a50c-ff469298ba71'] #SWC_NM_012 (poor/random stim trial performance)

pids_list_SNr_contra = ['b96ed9ce-1a0a-4818-b896-8aa79ca26801','b7998d00-b4c4-4695-8fc3-f8001539c90e', #SWC_NM_018 15/6, SWC_NM_018 16/6
                        'eb0937f5-951b-4bf8-9dc4-83ed776a1503', #SWC_NM_018 17/6 (few trials)
                        '3f9ff280-98b2-478a-b38f-b49294923756', #SWC_NM_021 24/3
                        '06cdb7a7-df86-48ea-8533-b1e383436987', 'a9c28dc5-6e1d-4750-8fff-1113ed26e6e9'] # SWC_NM_016
pids_list_SNr_contra_trained = ['b96ed9ce-1a0a-4818-b896-8aa79ca26801','b7998d00-b4c4-4695-8fc3-f8001539c90e', #SWC_NM_018 15/6, SWC_NM_018 16/6
                                'eb0937f5-951b-4bf8-9dc4-83ed776a1503'] #SWC_NM_018 17/6 (few trials) - shit session

excitation_trials_range_list_SNr = [list(range(242,364)) + list(range(461,581)) + list(range(674,769)), #SWC_NM_018 15/6
                                    list(range(283,423)) + list(range(528,660)) + list(range(767,833)), #SWC_NM_018 16/6
                                    list(range(371,422)) + list(range(485,501)), #SWC_NM_018 17/6
                                    list(range(180,369)), #SWC_NM_012
                                    list(range(83,136)) + list(range(207,269)) + list(range(296,315)), #SWC_NM_021 22/3
                                    list(range(67,169)) + list(range(283,370)), #SWC_NM_021 24/3
                                    list(range(50,100)) + list(range(150,230)), # SWC_NM_016
                                    list(range(69,197)) + list(range(320,473)), # SWC_NM_016
                                    list(range(54,138)) + list(range(193,276)) + list(range(358,403))] #SWC_NM_021 SNr 23/3/22

inhibition_trials_range_list_SNr = [list(range(139,242)) + list(range(364,461)) + list(range(581,674)) + list(range(769,798)), #SWC_NM_018 15/6
                                    list(range(121,283)) + list(range(423,528)) + list(range(660,767)), #SWC_NM_018 16/6
                                    list(range(422,485)), #SWC_NM_018 17/6
                                    list(range(75,180)), #SWC_NM_012
                                    list(range(0,83)) + list(range(269,296)), #SWC_NM_021 22/3
                                    list(range(0,67)) + list(range(169,283)), #SWC_NM_021 24/3
                                    list(range(0,50)) + list(range(100,150)) + list(range(230,304)), # SWC_NM_016
                                    list(range(0,69)) + list(range(197,320)), # SWC_NM_016
                                    list(range(0,54)) + list(range(140,193)) + list(range(276,358))] #SWC_NM_021 SNr 23/3/22
excitation_trials_range_list_SNr_trained = [list(range(242,364)) + list(range(461,581)) + list(range(674,769)), #SWC_NM_018 15/6
                                    list(range(283,423)) + list(range(528,660)) + list(range(767,833)), #SWC_NM_018 16/6
                                    list(range(371,422)) + list(range(485,501)), #SWC_NM_018 17/6
                                    list(range(180,369))] #SWC_NM_012]

inhibition_trials_range_list_SNr_trained = [list(range(139,242)) + list(range(364,461)) + list(range(581,674)) + list(range(769,798)), #SWC_NM_018 15/6
                                    list(range(121,283)) + list(range(423,528)) + list(range(660,767)), #SWC_NM_018 16/6
                                    list(range(422,485)), #SWC_NM_018 17/6
                                    list(range(75,180))] #SWC_NM_012

excitation_trials_range_list_SNr_contra = [list(range(242,364)) + list(range(461,581)) + list(range(674,769)), #SWC_NM_018 15/6
                                    list(range(283,423)) + list(range(528,660)) + list(range(767,833)), #SWC_NM_018 16/6
                                    list(range(371,422)) + list(range(485,501)), #SWC_NM_018 17/6
                                    list(range(67,169)) + list(range(283,370)), #SWC_NM_021 24/3
                                    list(range(50,100)) + list(range(150,230)), # SWC_NM_016
                                    list(range(69,197)) + list(range(320,473))] # SWC_NM_016
inhibition_trials_range_list_SNr_contra = [list(range(139,242)) + list(range(364,461)) + list(range(581,674)) + list(range(769,798)), #SWC_NM_018 15/6
                                    list(range(121,283)) + list(range(423,528)) + list(range(660,767)), #SWC_NM_018 16/6
                                    list(range(422,485)), #SWC_NM_018 17/6
                                    list(range(0,67)) + list(range(169,283)), #SWC_NM_021 24/3
                                    list(range(0,50)) + list(range(100,150)) + list(range(230,304)), # SWC_NM_016
                                    list(range(0,69)) + list(range(197,320))] # SWC_NM_016
excitation_trials_range_list_SNr_contra_trained = [list(range(242,364)) + list(range(461,581)) + list(range(674,769)), #SWC_NM_018 15/6
                                    list(range(283,423)) + list(range(528,660)) + list(range(767,833)), #SWC_NM_018 16/6
                                    list(range(371,422)) + list(range(485,501))] #SWC_NM_018 17/6
inhibition_trials_range_list_SNr_contra_trained = [list(range(139,242)) + list(range(364,461)) + list(range(581,674)) + list(range(769,798)), #SWC_NM_018 15/6
                                    list(range(121,283)) + list(range(423,528)) + list(range(660,767)), #SWC_NM_018 16/6
                                    list(range(422,485))] #SWC_NM_018 17/6

light_artifact_units_SNr = [[0,3,4,5,6,7,8],[[62,125,227]], #SWC_NM_018 16/6
                            [83,87,125,148,153],[],[38,86,193,283],[],[],[], #SWC_NM_018 17/6, #SWC_NM_021 22/3
                            [1,4,5,10,11,59,162,173,175,206]]

light_artifact_units_SNr_trained = [[0,3,4,5,6,7,8],[[62,125,227]], #SWC_NM_018 16/6
                                    [83,87,125,148,153],[]] #SWC_NM_018 17/6, SWC_NM_012

light_artifact_units_SNr_contra = [[127,128,146,147,203], #SWC_NM_018 15/6
                                    [3,119,139,148,178,187,244,254,255,258], #SWC_NM_018 16/6
                                    [],[],[],
                                    [11,66,415,420,422]] #SWC_NM_016 23/6

light_artifact_units_SNr_contra_trained = [[127,128,146,147,203], #SWC_NM_018 15/6
                                    [3,119,139,148,178,187,244,254,255,258], #SWC_NM_018 16/6
                                    [84,219]]

pids_list_ZI = ['0022179b-0101-48b0-b60f-c5de8ed3761d', 'ccfb329e-c3b0-43be-9710-5d7c8ee968d2',  #SWC_NM_020 22/3/22, #SWC_NM_020 23/3/22 (mostly ZI/thal, but also lots of MB units)
                'ddeb1b23-1c38-486c-83a9-237a81df6aaa', '6f890ac3-0ac7-441b-9896-515124ab2035', #SWC_NM_020 24/3/22, #SWC_NM_023 24/8/22
                'ebc4d953-abc5-4a3a-9232-1cf887221cda', '0157a7f7-1c57-4753-b8b6-94b38ff7d0b2', #SWC_NM_023 25/8/22, #SWC_NM_023 26/8/22
                'a7950dbb-440d-44ee-a544-815102413f6b', 'a50347db-d016-4d22-bde4-f03bbf4d2818', #SWC_NM_028 28/9, #SWC_NM_028 29/9
                '0d26b5b4-e951-49f5-a0b5-2c62f46d4c63', 'f54b959b-fee4-4130-951e-e366d34a5cbc', #SWC_NM_022 21/9, #SWC_NM_022 22/9
                '7f712873-42c8-42bc-a782-76b03ae3fb0f'] #SWC_NM_022 23/9

pids_list_ZI_contra = ['5eeb32c2-3eef-4b77-8647-3916629577cb','52ed488c-0cbe-4518-880f-c52c162a8999', #SWC_NM_020 24/3/22, #SWC_NM_022 21/9
                       '1579269a-17c2-46ef-a14e-448217386454', '7f94e86e-3a8b-4026-b120-89eeadf45a8d'] #SWC_NM_022 22/9, #SWC_NM_022 23/9

pids_list_ZI_trained = ['0d26b5b4-e951-49f5-a0b5-2c62f46d4c63', 'f54b959b-fee4-4130-951e-e366d34a5cbc', #SWC_NM_022 21/9, #SWC_NM_022 22/9
                        '7f712873-42c8-42bc-a782-76b03ae3fb0f'] #SWC_NM_022 23/9]

#### haven't looked through these well for artifact units
pids_list_ZI_trained_contra = ['52ed488c-0cbe-4518-880f-c52c162a8999', '1579269a-17c2-46ef-a14e-448217386454', #SWC_NM_022 21/9, #SWC_NM_022 22/9
                        '7f94e86e-3a8b-4026-b120-89eeadf45a8d'] #SWC_NM_022 23/9]

excitation_trials_range_list_ZI_trained = [
                                   list(range(0,172)) + list(range(458,674)), #SWC_NM_022 21/9
                                   list(range(0,246)) + list(range(514,699)), #SWC_NM_022 22/9
                                   list(range(130,328)) + list(range(510,637))] #SWC_NM_022 23/9

inhibition_trials_range_list_ZI_trained = [
                                   list(range(172,401)), #SWC_NM_022 21/9
                                   list(range(246,514)) + list(range(700,713)), #SWC_NM_022 22/9
                                   list(range(0,113)) + list(range(366,504))] #SWC_NM_022 23/9

excitation_trials_range_list_ZI_trained_contra = excitation_trials_range_list_ZI_trained
inhibition_trials_range_list_ZI_trained_contra = inhibition_trials_range_list_ZI_trained

light_artifact_units_ZI_trained = [
                           [26,99,169,172,222,405,886,1263,1361,1376], #SWC_NM_022 21/9
                           [55,197,278,352,640,1152,1196,1212], #SWC_NM_022 22/9
                           [73,177,597,770,780,781,784,855,1115]] #SWC_NM_022 23/9

light_artifact_units_ZI_trained_contra = [
                                  [49,296,327,593,692,1262,1263,1322], #SWC_NM_022 21/9
                                  [3,389,712,881,1195,1350], #SWC_NM_022 22/9
                                  [9,29,283,346,419,468,480,505,559,731,939,989,1385]] #SWC_NM_022 23/9

excitation_trials_range_list_ZI_directstim = [list(range(53,107)) + list(range(164,234)) + list(range(346,463)), #SWC_NM_023 25/8/22
                                              list(range(0,134)) + list(range(294,435)) + list(range(578,642)), #SWC_NM_023 26/8/22
                                              list(range(86,162)) + list(range(239,280)) + list(range(309,380)), #SWC_NM_020 23/3/22
                                              list(range(0,42)) + list(range(83,127)) + list(range(176,205)), #SWC_NM_028 28/9
                                              list(range(0,55)) + list(range(118,173)) + list(range(293,349)), #SWC_NM_028 29/9
                                              list(range(0,64)) + list(range(175,393)), #SWC_NM_032 16/1
                                              list(range(71,136)) + list(range(217,377)), #SWC_NM_032 17/1
                                              list(range(95,201)) + list(range(329,380)) + list(range(388,501))] #SWC_NM_032 18/1
inhibition_trials_range_list_ZI_directstim = [list(range(107,164)) + list(range(234,346)), #SWC_NM_023 25/8/22
                                              list(range(134,294)) + list(range(435,578)), #SWC_NM_023 26/8/22
                                              list(range(0,86)) + list(range(162,239)) + list(range(280,309)), #SWC_NM_020 23/3/22
                                              list(range(42,83)) + list(range(127,175)), #SWC_NM_028 28/9
                                              list(range(55,118)) + list(range(173,293)) + list(range(349,366)), #SWC_NM_028 29/9
                                              list(range(78,175)) + list(range(393,470)), #SWC_NM_032 16/1
                                              list(range(0,71)) + list(range(136,217)) + list(range(377,394)), #SWC_NM_032 17/1
                                              list(range(0,95)) + list(range(204,329)) + list(range(501,586))] #SWC_NM_032 18/1

excitation_trials_range_list_ZI = [list(range(0,94)) + list(range(174,218)) + list(range(282,321)), #SWC_NM_020 22/3/22
                                   list(range(86,162)) + list(range(239,280)) + list(range(309,380)), #SWC_NM_020 23/3/22
                                   list(range(55,110)) + list(range(156,202)) + list(range(292,358)), #SWC_NM_020 24/3/22
                                   list(range(0,111)) + list(range(255,318)), #SWC_NM_023 24/8/22
                                   list(range(53,107)) + list(range(164,234)) + list(range(346,463)), #SWC_NM_023 25/8/22
                                   list(range(0,134)) + list(range(294,435)) + list(range(578,642)), #SWC_NM_023 26/8/22
                                   list(range(0,42)) + list(range(83,127)) + list(range(176,205)), #SWC_NM_028 28/9
                                   list(range(0,55)) + list(range(118,173)) + list(range(293,349)), #SWC_NM_028 29/9
                                   list(range(0,172)) + list(range(458,674)), #SWC_NM_022 21/9
                                   list(range(0,246)) + list(range(514,699)), #SWC_NM_022 22/9
                                   list(range(130,328)) + list(range(510,637))] #SWC_NM_022 23/9

inhibition_trials_range_list_ZI = [list(range(94,174)) + list(range(218,282)) + list(range(321,323)), #SWC_NM_020 22/3/22
                                   list(range(0,86)) + list(range(162,239)) + list(range(280,309)), #SWC_NM_020 23/3/22
                                   list(range(0,55)) + list(range(110,156)) + list(range(206,236)) + list(range(255,292)), #SWC_NM_020 24/3/22
                                   list(range(111,255)) + list(range(318,338)), #SWC_NM_023 24/8/22
                                   list(range(107,164)) + list(range(234,346)), #SWC_NM_023 25/8/22
                                   list(range(134,294)) + list(range(435,578)), #SWC_NM_023 26/8/22
                                   list(range(42,83)) + list(range(127,175)), #SWC_NM_028 28/9
                                   list(range(55,118)) + list(range(173,293)) + list(range(349,366)), #SWC_NM_028 29/9
                                   list(range(172,401)), #SWC_NM_022 21/9
                                   list(range(246,514)) + list(range(700,713)), #SWC_NM_022 22/9
                                   list(range(0,113)) + list(range(366,504))] #SWC_NM_022 23/9

excitation_trials_range_list_ZI_contra = [list(range(55,110)) + list(range(156,202)) + list(range(292,358)), #SWC_NM_020 24/3/22
                                          list(range(0,172)) + list(range(458,674)), #SWC_NM_022 21/9
                                          list(range(0,246)) + list(range(514,699)), #SWC_NM_022 22/9
                                          list(range(130,328)) + list(range(510,637))] #SWC_NM_022 23/9

inhibition_trials_range_list_ZI_contra = [list(range(0,55)) + list(range(110,156)) + list(range(206,236)) + list(range(255,292)), #SWC_NM_020 24/3/22
                                          list(range(172,401)), #SWC_NM_022 21/9
                                          list(range(246,514)) + list(range(700,713)), #SWC_NM_022 22/9
                                          list(range(0,113)) + list(range(366,504))] #SWC_NM_022 23/9

light_artifact_units_ZI = [[0,9,55,62,80,81,94,103,104,121,125,135,140,146,150,155,157,176,181,185,197,205,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,283], #SWC_NM_020 22/3/22
                           [102,126,127,366], #SWC_NM_020 23/3/22
                           [125],[22],[],[], #SWC_NM_020 24/3/22, #SWC_NM_023 24/8/22
                           [],[1222,1251],
                           [26,99,172,222,405,1263,1361,1376], #SWC_NM_022 21/9
                           [55,197,278,352,640,1152], #SWC_NM_022 22/9
                           [73,177,1115]] #SWC_NM_022 23/9

light_artifact_units_ZI_contra = [[],
                                  [49,296,327,593,692,1262,1263,1322], #SWC_NM_022 21/9
                                  [3,389,712,881,1195,1350], #SWC_NM_022 22/9
                                  [9,29,283,346,419,468,480,505,559,731,939,989,1385]] #SWC_NM_022 23/9

light_artifact_units_ZI_directstim =  [[23,35,55,97,162,206,369] + list(range(282,332)), #SWC_NM_023 25/8/22, #Questionable:35
                                       [0,13,14,38,46,47,81,93,98,126,135,202,206,268] + list(range(206,246)), #SWC_NM_023 26/8/22
                                       [77,80,93,102,106,107,126,127,321,339,364,365,366], #questionable:106
                                       [288,430,454,467,481],[288,386],
                                       [],[],[]] #SWC_NM_032
