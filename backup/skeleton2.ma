//Maya ASCII 2022 scene
//Name: skeleton2.ma
//Last modified: Sun, Apr 04, 2021 02:19:50 PM
//Codeset: 949
requires maya "2022";
requires -nodeType "HIKCharacterNode" -nodeType "HIKSkeletonGeneratorNode" -nodeType "HIKProperty2State"
		 -dataType "HIKCharacter" -dataType "HIKCharacterState" -dataType "HIKEffectorState"
		 -dataType "HIKPropertySetState" "mayaHIK" "1.0_HIK_2018.11";
requires "mtoa" "4.2.1";
currentUnit -l centimeter -a degree -t 120fps;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202102181415-29bfc1879c";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19042)";
fileInfo "UUID" "B7DB5B65-4311-4D94-CC12-DA9C87ED698B";
createNode transform -s -n "persp";
	rename -uid "D73CA07A-4015-F8D8-D45E-24B714DF8FF6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -21.428701364373612 130.23027146638398 135.71254965200077 ;
	setAttr ".r" -type "double3" 6.8616472703102662 -363.3999999999964 2.4891897471787964e-17 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "EB098E70-46AA-82DC-DE8E-64849E1F5EEE";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 123.7878481443569;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "23B35ABD-4A7F-7BFC-CCD4-C598AADC5389";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "14258CB8-4630-BB70-3285-3298F7A4F2C8";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "B309FE3C-44CE-7379-D6E2-D0A88DD3F285";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "40992A79-431B-EA84-CF9A-96A894C0B457";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "0BDDC7B3-4FCB-2C0D-6ADE-AB8BDB01E716";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D91F7E82-4900-6159-7BBB-80B5C8AC45EE";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "Character1_Reference";
	rename -uid "162EEEF2-4322-CF38-B9C1-879B0B4BF820";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
createNode locator -n "Character1_ReferenceShape" -p "Character1_Reference";
	rename -uid "C2F8F71B-45AB-7FAD-E8CF-CC986D532086";
	setAttr -k off ".v";
createNode joint -n "Character1_Hips" -p "Character1_Reference";
	rename -uid "2F976AB9-4CED-1A8D-9F07-9085E0B3091F";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 100 0 ;
	setAttr ".typ" 1;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftUpLeg" -p "Character1_Hips";
	rename -uid "B483F357-414E-9861-2E2D-12AB2BF0911A";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 8.9100008010000007 -6.2700004600000057 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftLeg" -p "Character1_LeftUpLeg";
	rename -uid "D1C71875-4DA9-FF57-262A-8F9DD3E44964";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 -44.878644939999994 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftFoot" -p "Character1_LeftLeg";
	rename -uid "B85F0D40-4E0C-B9DE-761B-739D36DE8668";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 -40.700958253000003 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftToeBase" -p "Character1_LeftFoot";
	rename -uid "627E274C-4F3F-0B7D-C18D-AFA807B87CBB";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 8.4269999991448685e-06 -6.2623171929999977 12.9547209 ;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightUpLeg" -p "Character1_Hips";
	rename -uid "DCF481CA-4EF1-C111-5BAC-658A333C8985";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -8.9100008010000007 -6.2700004600000057 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightLeg" -p "Character1_RightUpLeg";
	rename -uid "19EFBC5D-4200-B09B-238D-148D873472AD";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -2.715999999125529e-06 -44.878644939999994 0.00043902399999999999 ;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightFoot" -p "Character1_RightLeg";
	rename -uid "440AE61C-4767-903A-9D57-17ABC65790CB";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 9.1899999965505685e-07 -40.700958249000003 0 ;
	setAttr ".r" -type "double3" 0 -0.0048003860000000002 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightToeBase" -p "Character1_RightFoot";
	rename -uid "545395F7-446A-F49B-D293-7990F28F0248";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 7.9816864229087514e-10 -6.2623171799999993 12.954749111467956 ;
	setAttr ".r" -type "double3" 0.0029125930000000002 -0.0048003860000000002 0 ;
	setAttr ".jo" -type "double3" 0 0.028802316000000005 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 5;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_Spine" -p "Character1_Hips";
	rename -uid "9E6CD3E6-4E33-FE43-FDE0-A7B728A7102F";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 7 0 ;
	setAttr ".typ" 6;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_Spine1" -p "Character1_Spine";
	rename -uid "E6C935C1-4BE6-1801-26B8-D687D8354641";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 12.666666666666671 0 ;
	setAttr ".typ" 6;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_Spine2" -p "Character1_Spine1";
	rename -uid "ED82CD5A-4546-BDE1-F41B-898E37547275";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 12.666666666666671 0 ;
	setAttr ".typ" 6;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftShoulder" -p "Character1_Spine2";
	rename -uid "524A29CF-435B-3BDA-4C8A-C9A789B0E8CC";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 7.0000004770000004 14.255213466666646 0 ;
	setAttr ".r" -type "double3" 0 0 0.00073528199999999997 ;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftArm" -p "Character1_LeftShoulder";
	rename -uid "44274F5D-4CFA-64C6-E1D8-4CAD35D111A6";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".jo" -type "double3" 0 0 -0.0044116919999999983 ;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftForeArm" -p "Character1_LeftArm";
	rename -uid "1A60B4A7-44F6-DBE6-67A7-C486495B6E3D";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 6.3771943928806802 19.582541568063096 -83.078639106980418 ;
	setAttr ".jo" -type "double3" 0 0 0.011029229999999999 ;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftHand" -p "Character1_LeftForeArm";
	rename -uid "69803ED9-4A6E-75EF-0AA3-1F906C6FD670";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 26.697 0 0 ;
	setAttr ".jo" -type "double3" 0 0 -0.014705640000000002 ;
	setAttr ".sd" 1;
	setAttr ".typ" 12;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_LeftHandThumb1" -p "Character1_LeftHand";
	rename -uid "365C71A2-462A-2BC2-1FCE-AB9F821E98AC";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 4.349 -0.799 4.282 ;
	setAttr ".jo" -type "double3" 0 0 0.011029230000000003 ;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "Character1_LeftHandThumb2" -p "Character1_LeftHandThumb1";
	rename -uid "8CE5302E-4E2B-6C91-4747-7283AC658148";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.513 -0.536 0.707 ;
	setAttr ".r" -type "double3" 0 0 -0.00029786199999999997 ;
	setAttr ".jo" -type "double3" 0 0 -0.0044116920000000009 ;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "Character1_LeftHandThumb3" -p "Character1_LeftHandThumb2";
	rename -uid "7633B317-4113-FF45-EB9B-068839AB2F9F";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.543 0 0 ;
	setAttr ".jo" -type "double3" 0 0 0.0025224540000000004 ;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "Character1_LeftHandThumb4" -p "Character1_LeftHandThumb3";
	rename -uid "C504B77D-4A09-7B03-DD5F-64B85A14286F";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.677 0 0 ;
	setAttr ".jo" -type "double3" 0 0 -0.0044679299999999993 ;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "Character1_LeftHandIndex1" -p "Character1_LeftHand";
	rename -uid "AE1812EC-4204-9F08-2117-759733DBB92E";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 8.822 0.2 3.472 ;
	setAttr ".r" -type "double3" 0 -2 0 ;
	setAttr ".jo" -type "double3" 0 0 0.011029230000000003 ;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "Character1_LeftHandIndex2" -p "Character1_LeftHandIndex1";
	rename -uid "96FAD3DA-4D07-C135-144E-7D83820B5151";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 4.225 0 0 ;
	setAttr ".r" -type "double3" 0 -2 0 ;
	setAttr ".jo" -type "double3" 3.9767686272416974e-05 11.999999906916589 -0.0026199006522314512 ;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "Character1_LeftHandIndex3" -p "Character1_LeftHandIndex2";
	rename -uid "C7B9A47F-4EE6-45FD-AAFF-F1AF4D3D3291";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.647 0 0.185 ;
	setAttr ".r" -type "double3" 0 -2 0 ;
	setAttr ".jo" -type "double3" 0.00031182480137193966 -17.999999861621749 -0.0020221329458448675 ;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "Character1_LeftHandIndex4" -p "Character1_LeftHandIndex3";
	rename -uid "DFCF6F28-44D1-D482-D45A-DE825B5F58FA";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 1.957 0 0.068 ;
	setAttr ".r" -type "double3" 0 -2 0 ;
	setAttr ".jo" -type "double3" 0.00073387615628503857 21.999999820320067 0.0034761245573327409 ;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "Character1_LeftHandMiddle1" -p "Character1_LeftHand";
	rename -uid "DEAE7FE8-4B58-82B6-F9B2-348F11F31E08";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 8.81 0.501 1.305 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" 0 0 0.011029230000000003 ;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "Character1_LeftHandMiddle2" -p "Character1_LeftHandMiddle1";
	rename -uid "04719F73-455E-EAAF-7173-26B834372AFA";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 4.863 0 0 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" -2.7437157412159982e-07 0.021380003989143481 -0.0044116921066480802 ;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "Character1_LeftHandMiddle3" -p "Character1_LeftHandMiddle2";
	rename -uid "79F74B92-48EA-6796-CE68-F09AC4C40BF3";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.765 0 0 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" -4.5728601627035792e-07 -0.032070005995011877 0.00073528226306528079 ;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "Character1_LeftHandMiddle4" -p "Character1_LeftHandMiddle3";
	rename -uid "6F92279F-4A86-704B-0AE0-D98840FB3D10";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.006 0 0 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" -4.5728612239275568e-07 0.039196674000000008 -2.8439495905273179e-10 ;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "Character1_LeftHandRing1" -p "Character1_LeftHand";
	rename -uid "9A700840-460E-5C61-1443-1C91CE5464E1";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 8.894 0.38 -0.793 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" 0 0 0.011029230000000003 ;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "Character1_LeftHandRing2" -p "Character1_LeftHandRing1";
	rename -uid "776522F5-4A82-2810-C70B-4EA678BFD929";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 4.538 0 0 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" -2.7438658884226412e-07 0.021381173989142875 -0.0044116921066597444 ;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "Character1_LeftHandRing3" -p "Character1_LeftHandRing2";
	rename -uid "B52B63F8-4FA8-9A74-50FE-B5A07676E861";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 2.305 0 0 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" -4.5731104081453454e-07 -0.032071760995011578 0.00073528226309407222 ;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "Character1_LeftHandRing4" -p "Character1_LeftHandRing3";
	rename -uid "95629107-403F-6F96-7D6D-ECBE1D37CDCB";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 1.923 0 0 ;
	setAttr ".r" -type "double3" 0 -0.004 0 ;
	setAttr ".jo" -type "double3" -4.5731114695435592e-07 0.039198818999999982 -2.8442608627698344e-10 ;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "Character1_LeftHandPinky1" -p "Character1_LeftHand";
	rename -uid "7B5BA24F-456E-3C60-47C4-E99EAA49A385";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 8.882 -0.313 -2.49 ;
	setAttr ".r" -type "double3" 0 0 0.001 ;
	setAttr ".jo" -type "double3" 0 0 0.011029230000000003 ;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "Character1_LeftHandPinky2" -p "Character1_LeftHandPinky1";
	rename -uid "DABB5446-4C72-D613-B7E9-AB84913D4AB0";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 3.044 0 0 ;
	setAttr ".r" -type "double3" 0 0 0.001 ;
	setAttr ".jo" -type "double3" 0 0 -0.0089898479999999999 ;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "Character1_LeftHandPinky3" -p "Character1_LeftHandPinky2";
	rename -uid "DAA35E87-463C-6BB7-D2FF-20B3DE76E8EB";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 1.975 0 0 ;
	setAttr ".r" -type "double3" 0 0 0.001 ;
	setAttr ".jo" -type "double3" 0 0 0.0076025159999999958 ;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "Character1_LeftHandPinky4" -p "Character1_LeftHandPinky3";
	rename -uid "E44B4491-4F15-EF62-C071-0D89AA5DBFB9";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 1.667 0 0 ;
	setAttr ".r" -type "double3" 0 0 0.001 ;
	setAttr ".jo" -type "double3" 0 0 -0.0083932859999999981 ;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "Character1_RightShoulder" -p "Character1_Spine2";
	rename -uid "BFD3BFEF-46AC-9D4F-74DE-1B85B99C8BD9";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -6.9999995229999996 14.255213466666646 0 ;
	setAttr ".r" -type "double3" 0 0 -0.0023183610000000001 ;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightArm" -p "Character1_RightShoulder";
	rename -uid "883B7ADB-4F7B-06A9-C667-5B91D18C81B4";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".jo" -type "double3" 0 0 0.013910165999999998 ;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightForeArm" -p "Character1_RightArm";
	rename -uid "33F7145E-4825-1883-97A1-56BCB67225D5";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".jo" -type "double3" 0 0 -0.03477541499999999 ;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightHand" -p "Character1_RightForeArm";
	rename -uid "1E790156-4131-B81C-9190-3CBECAA28676";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".jo" -type "double3" 0 0 0.046367219999999987 ;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_RightHandThumb1" -p "Character1_RightHand";
	rename -uid "F4E8095D-475B-4EDF-85D1-9D8D0E40F6EC";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".jo" -type "double3" 0 0 -0.034775415000000004 ;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
createNode joint -n "Character1_RightHandThumb2" -p "Character1_RightHandThumb1";
	rename -uid "CD32C772-461B-49EA-97B9-A5A262156D78";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.00060208600000000005 ;
	setAttr ".jo" -type "double3" 0 0 0.013910166000000003 ;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
createNode joint -n "Character1_RightHandThumb3" -p "Character1_RightHandThumb2";
	rename -uid "6B5D6631-454F-C49A-B101-1CB680EE93B7";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.00039149399999999999 ;
	setAttr ".jo" -type "double3" 0 0 0.0012941549999999965 ;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
createNode joint -n "Character1_RightHandThumb4" -p "Character1_RightHandThumb3";
	rename -uid "54C37B21-420A-B7DA-8533-259009EA8EBA";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.00039149399999999999 ;
	setAttr ".jo" -type "double3" 0 0 -0.0066823259999999989 ;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
createNode joint -n "Character1_RightHandIndex1" -p "Character1_RightHand";
	rename -uid "709F6737-4C9C-5970-1B69-2AA397C50B54";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 2 0 ;
	setAttr ".jo" -type "double3" 0 0 -0.034775415000000004 ;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
createNode joint -n "Character1_RightHandIndex2" -p "Character1_RightHandIndex1";
	rename -uid "8DDA988F-4E80-77E5-8D20-5F8A7966B097";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 2 0 ;
	setAttr ".jo" -type "double3" 0.00057893916151730137 12.000387886911755 0.014017828407258326 ;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
createNode joint -n "Character1_RightHandIndex3" -p "Character1_RightHandIndex2";
	rename -uid "E27C7EB1-4B6F-5DD5-E21A-65A916C56A45";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 2 0 ;
	setAttr ".jo" -type "double3" 0.00025481484529355864 -18.000581982957364 -0.0023844045345728028 ;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
createNode joint -n "Character1_RightHandIndex4" -p "Character1_RightHandIndex3";
	rename -uid "9EF25BC8-4F9A-D2EC-7824-79973F7665EB";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 2 0 ;
	setAttr ".jo" -type "double3" -3.0848417334584165e-18 22.000711171999988 -4.1374294274114837e-19 ;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
createNode joint -n "Character1_RightHandMiddle1" -p "Character1_RightHand";
	rename -uid "56AE67C6-4018-7D7C-DCE8-84BAB9ED0BA1";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" 0 0 -0.034775415000000004 ;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
createNode joint -n "Character1_RightHandMiddle2" -p "Character1_RightHandMiddle1";
	rename -uid "1312039A-4851-BD85-5B87-7996E5DA750E";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" 0.00057893916151730137 12.000387886911755 0.014017828407258326 ;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
createNode joint -n "Character1_RightHandMiddle3" -p "Character1_RightHandMiddle2";
	rename -uid "CD8D6E7C-4F79-202C-8DE4-DE9142B61A9A";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" 0.00025481484529355864 -18.000581982957364 -0.0023844045345728028 ;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
createNode joint -n "Character1_RightHandMiddle4" -p "Character1_RightHandMiddle3";
	rename -uid "6B48BC90-446F-A734-CF1A-74A447A16543";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" -3.0848417334584165e-18 22.000711171999988 -4.1374294274114837e-19 ;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
createNode joint -n "Character1_RightHandRing1" -p "Character1_RightHand";
	rename -uid "73FCA6DE-434C-DB61-D452-2492DDCF1548";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" 0 0 -0.034775415000000004 ;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
createNode joint -n "Character1_RightHandRing2" -p "Character1_RightHandRing1";
	rename -uid "CBA93FDB-4A51-3BAF-33F3-3F97F1FEC761";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" 0.00057893916151730137 12.000387886911755 0.014017828407258326 ;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
createNode joint -n "Character1_RightHandRing3" -p "Character1_RightHandRing2";
	rename -uid "ACF2E936-416B-A451-56B6-8C8356BDD41D";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" 0.00025481484529355864 -18.000581982957364 -0.0023844045345728028 ;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
createNode joint -n "Character1_RightHandRing4" -p "Character1_RightHandRing3";
	rename -uid "300B3E3C-4B85-795F-C97A-F097DC27BF78";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0.004 0 ;
	setAttr ".jo" -type "double3" -3.0848417334584165e-18 22.000711171999988 -4.1374294274114837e-19 ;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
createNode joint -n "Character1_RightHandPinky1" -p "Character1_RightHand";
	rename -uid "F0C72C47-499A-6DAD-E2AA-848B0AD39079";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.001 ;
	setAttr ".jo" -type "double3" 0 0 -0.034775415000000004 ;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
createNode joint -n "Character1_RightHandPinky2" -p "Character1_RightHandPinky1";
	rename -uid "39421291-4DA5-77D6-7587-28AB9E3370AA";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.001 ;
	setAttr ".jo" -type "double3" -0.0003473165155227558 12.000387916518784 0.0064465962630108299 ;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
createNode joint -n "Character1_RightHandPinky3" -p "Character1_RightHandPinky2";
	rename -uid "0961FEC7-4325-7441-D48E-F391042C830C";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.001 ;
	setAttr ".jo" -type "double3" -0.0013733125576394611 -18.000581921549415 0.009136064439409123 ;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
createNode joint -n "Character1_RightHandPinky4" -p "Character1_RightHandPinky3";
	rename -uid "22ABCA2D-4C0B-E15B-A122-9E9C4723E99C";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".r" -type "double3" 0 0 -0.001 ;
	setAttr ".jo" -type "double3" -0.0030431224584647996 22.000710919592766 -0.014413774206572399 ;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
createNode joint -n "Character1_Neck" -p "Character1_Spine2";
	rename -uid "961BA13F-45F7-4F08-CAB8-A5834C7224E7";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 12.666666666666657 0 ;
	setAttr ".typ" 7;
	setAttr ".radi" 1.5;
createNode joint -n "Character1_Head" -p "Character1_Neck";
	rename -uid "7DEDFC1E-4336-4576-DA5B-9196B2EC92AC";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 0 20 0 ;
	setAttr ".typ" 8;
	setAttr ".radi" 1.5;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "DE12704B-4AC0-C645-51FF-6483C9BC6D9E";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "EDED729F-40A7-39FD-68CB-E089755998D7";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "423FCBE5-47BD-F179-3578-C0BF2724A7CA";
createNode displayLayerManager -n "layerManager";
	rename -uid "8E97D509-46E7-F1E5-4901-37872B6D69E4";
createNode displayLayer -n "defaultLayer";
	rename -uid "96707C68-4087-6202-5451-75A66B54C101";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "F5110A95-4CBE-E348-A02A-34BBBCB774F1";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "3D513206-447D-DEC3-289B-58A0C7836032";
	setAttr ".g" yes;
createNode HIKCharacterNode -n "Character1";
	rename -uid "9E08D82F-4528-343B-5A5E-8495FDFD20D6";
	setAttr ".OutputCharacterDefinition" -type "HIKCharacter" ;
	setAttr ".ReferenceMinRLimitx" -45;
	setAttr ".ReferenceMinRLimity" -45;
	setAttr ".ReferenceMinRLimitz" -45;
	setAttr ".ReferenceMaxRLimitx" 45;
	setAttr ".ReferenceMaxRLimity" 45;
	setAttr ".ReferenceMaxRLimitz" 45;
	setAttr ".HipsTy" 100;
	setAttr ".HipsMinRLimitx" -45;
	setAttr ".HipsMinRLimity" -45;
	setAttr ".HipsMinRLimitz" -45;
	setAttr ".HipsMaxRLimitx" 45;
	setAttr ".HipsMaxRLimity" 45;
	setAttr ".HipsMaxRLimitz" 45;
	setAttr ".LeftUpLegTx" 8.9100008010000007;
	setAttr ".LeftUpLegTy" 93.729999539999994;
	setAttr ".LeftUpLegMinRLimitx" -45;
	setAttr ".LeftUpLegMinRLimity" -45;
	setAttr ".LeftUpLegMinRLimitz" -45;
	setAttr ".LeftUpLegMaxRLimitx" 45;
	setAttr ".LeftUpLegMaxRLimity" 45;
	setAttr ".LeftUpLegMaxRLimitz" 45;
	setAttr ".LeftLegTx" 8.9100008010000007;
	setAttr ".LeftLegTy" 48.851354600000001;
	setAttr ".LeftLegMinRLimitx" -45;
	setAttr ".LeftLegMinRLimity" -45;
	setAttr ".LeftLegMinRLimitz" -45;
	setAttr ".LeftLegMaxRLimitx" 45;
	setAttr ".LeftLegMaxRLimity" 45;
	setAttr ".LeftLegMaxRLimitz" 45;
	setAttr ".LeftFootTx" 8.9100008010000007;
	setAttr ".LeftFootTy" 8.1503963469999974;
	setAttr ".LeftFootMinRLimitx" -45;
	setAttr ".LeftFootMinRLimity" -45;
	setAttr ".LeftFootMinRLimitz" -45;
	setAttr ".LeftFootMaxRLimitx" 45;
	setAttr ".LeftFootMaxRLimity" 45;
	setAttr ".LeftFootMaxRLimitz" 45;
	setAttr ".RightUpLegTx" -8.9100008010000007;
	setAttr ".RightUpLegTy" 93.729999539999994;
	setAttr ".RightUpLegMinRLimitx" -45;
	setAttr ".RightUpLegMinRLimity" -45;
	setAttr ".RightUpLegMinRLimitz" -45;
	setAttr ".RightUpLegMaxRLimitx" 45;
	setAttr ".RightUpLegMaxRLimity" 45;
	setAttr ".RightUpLegMaxRLimitz" 45;
	setAttr ".RightLegTx" -8.9100035169999998;
	setAttr ".RightLegTy" 48.851354600000001;
	setAttr ".RightLegTz" 0.00043902399999999999;
	setAttr ".RightLegMinRLimitx" -45;
	setAttr ".RightLegMinRLimity" -45;
	setAttr ".RightLegMinRLimitz" -45;
	setAttr ".RightLegMaxRLimitx" 45;
	setAttr ".RightLegMaxRLimity" 45;
	setAttr ".RightLegMaxRLimitz" 45;
	setAttr ".RightFootTx" -8.9100025980000002;
	setAttr ".RightFootTy" 8.1503963509999977;
	setAttr ".RightFootTz" 0.00043902399999999999;
	setAttr ".RightFootRy" -0.0048003860000000002;
	setAttr ".RightFootMinRLimitx" -45;
	setAttr ".RightFootMinRLimity" -45;
	setAttr ".RightFootMinRLimitz" -45;
	setAttr ".RightFootMaxRLimitx" 45;
	setAttr ".RightFootMaxRLimity" 45;
	setAttr ".RightFootMaxRLimitz" 45;
	setAttr ".SpineTy" 107;
	setAttr ".SpineMinRLimitx" -45;
	setAttr ".SpineMinRLimity" -45;
	setAttr ".SpineMinRLimitz" -45;
	setAttr ".SpineMaxRLimitx" 45;
	setAttr ".SpineMaxRLimity" 45;
	setAttr ".SpineMaxRLimitz" 45;
	setAttr ".LeftArmTx" 17.707251070000005;
	setAttr ".LeftArmTy" 146.58868419999996;
	setAttr ".LeftArmRz" -0.0036764099999999984;
	setAttr ".LeftArmJointOrientz" -0.0044116919999999983;
	setAttr ".LeftArmMinRLimitx" -45;
	setAttr ".LeftArmMinRLimity" -45;
	setAttr ".LeftArmMinRLimitz" -45;
	setAttr ".LeftArmMaxRLimitx" 45;
	setAttr ".LeftArmMaxRLimity" 45;
	setAttr ".LeftArmMaxRLimitz" 45;
	setAttr ".LeftForeArmTx" 45.012716770000004;
	setAttr ".LeftForeArmTy" 146.58868419999999;
	setAttr ".LeftForeArmRz" 0.0073528200000000012;
	setAttr ".LeftForeArmJointOrientz" 0.011029229999999999;
	setAttr ".LeftForeArmMinRLimitx" -45;
	setAttr ".LeftForeArmMinRLimity" -45;
	setAttr ".LeftForeArmMinRLimitz" -45;
	setAttr ".LeftForeArmMaxRLimitx" 45;
	setAttr ".LeftForeArmMaxRLimity" 45;
	setAttr ".LeftForeArmMaxRLimitz" 45;
	setAttr ".LeftHandTx" 71.709864140000008;
	setAttr ".LeftHandTy" 146.58868419999999;
	setAttr ".LeftHandRz" -0.007352820000000003;
	setAttr ".LeftHandSx" 0.99999999999999989;
	setAttr ".LeftHandSy" 0.99999999999999989;
	setAttr ".LeftHandJointOrientz" -0.014705640000000002;
	setAttr ".LeftHandMinRLimitx" -45;
	setAttr ".LeftHandMinRLimity" -45;
	setAttr ".LeftHandMinRLimitz" -45;
	setAttr ".LeftHandMaxRLimitx" 45;
	setAttr ".LeftHandMaxRLimity" 45;
	setAttr ".LeftHandMaxRLimitz" 45;
	setAttr ".RightArmTx" -17.707274910000002;
	setAttr ".RightArmTy" 146.58898000000002;
	setAttr ".RightArmRz" 0.011591805;
	setAttr ".RightArmSx" 0.99999999999999989;
	setAttr ".RightArmSy" 0.99999999999999989;
	setAttr ".RightArmJointOrientz" 0.013910165999999998;
	setAttr ".RightArmMinRLimitx" -45;
	setAttr ".RightArmMinRLimity" -45;
	setAttr ".RightArmMinRLimitz" -45;
	setAttr ".RightArmMaxRLimitx" 45;
	setAttr ".RightArmMaxRLimity" 45;
	setAttr ".RightArmMaxRLimitz" 45;
	setAttr ".RightForeArmTx" -45.012873159999998;
	setAttr ".RightForeArmTy" 146.58898;
	setAttr ".RightForeArmRz" -0.02318360999999999;
	setAttr ".RightForeArmSx" 0.99999999999999989;
	setAttr ".RightForeArmSy" 0.99999999999999989;
	setAttr ".RightForeArmJointOrientz" -0.03477541499999999;
	setAttr ".RightForeArmMinRLimitx" -45;
	setAttr ".RightForeArmMinRLimity" -45;
	setAttr ".RightForeArmMinRLimitz" -45;
	setAttr ".RightForeArmMaxRLimitx" 45;
	setAttr ".RightForeArmMaxRLimity" 45;
	setAttr ".RightForeArmMaxRLimitz" 45;
	setAttr ".RightHandTx" -71.709861270000005;
	setAttr ".RightHandTy" 146.58897870000001;
	setAttr ".RightHandRz" 0.02318361;
	setAttr ".RightHandSx" 0.99999999999999978;
	setAttr ".RightHandSy" 0.99999999999999978;
	setAttr ".RightHandJointOrientz" 0.046367219999999987;
	setAttr ".RightHandMinRLimitx" -45;
	setAttr ".RightHandMinRLimity" -45;
	setAttr ".RightHandMinRLimitz" -45;
	setAttr ".RightHandMaxRLimitx" 45;
	setAttr ".RightHandMaxRLimity" 45;
	setAttr ".RightHandMaxRLimitz" 45;
	setAttr ".HeadTy" 165;
	setAttr ".HeadMinRLimitx" -45;
	setAttr ".HeadMinRLimity" -45;
	setAttr ".HeadMinRLimitz" -45;
	setAttr ".HeadMaxRLimitx" 45;
	setAttr ".HeadMaxRLimity" 45;
	setAttr ".HeadMaxRLimitz" 45;
	setAttr ".LeftToeBaseTx" 8.9100092279999998;
	setAttr ".LeftToeBaseTy" 1.8880791539999997;
	setAttr ".LeftToeBaseTz" 12.9547209;
	setAttr ".LeftToeBaseMinRLimitx" -45;
	setAttr ".LeftToeBaseMinRLimity" -45;
	setAttr ".LeftToeBaseMinRLimitz" -45;
	setAttr ".LeftToeBaseMaxRLimitx" 45;
	setAttr ".LeftToeBaseMaxRLimity" 45;
	setAttr ".LeftToeBaseMaxRLimitz" 45;
	setAttr ".RightToeBaseTx" -8.9110879790000013;
	setAttr ".RightToeBaseTy" 1.8880791709999984;
	setAttr ".RightToeBaseTz" 12.955188090000002;
	setAttr ".RightToeBaseRx" 0.0029125930000000011;
	setAttr ".RightToeBaseRy" 0.019201544000000011;
	setAttr ".RightToeBaseSy" 0.99999999999999989;
	setAttr ".RightToeBaseJointOrienty" 0.028802316000000005;
	setAttr ".RightToeBaseMinRLimitx" -45;
	setAttr ".RightToeBaseMinRLimity" -45;
	setAttr ".RightToeBaseMinRLimitz" -45;
	setAttr ".RightToeBaseMaxRLimitx" 45;
	setAttr ".RightToeBaseMaxRLimity" 45;
	setAttr ".RightToeBaseMaxRLimitz" 45;
	setAttr ".LeftShoulderTx" 7.0000004770000004;
	setAttr ".LeftShoulderTy" 146.58854679999999;
	setAttr ".LeftShoulderRz" 0.00073528200000000008;
	setAttr ".LeftShoulderMinRLimitx" -45;
	setAttr ".LeftShoulderMinRLimity" -45;
	setAttr ".LeftShoulderMinRLimitz" -45;
	setAttr ".LeftShoulderMaxRLimitx" 45;
	setAttr ".LeftShoulderMaxRLimity" 45;
	setAttr ".LeftShoulderMaxRLimitz" 45;
	setAttr ".RightShoulderTx" -6.9999995229999996;
	setAttr ".RightShoulderTy" 146.58854679999999;
	setAttr ".RightShoulderRz" -0.0023183610000000006;
	setAttr ".RightShoulderMinRLimitx" -45;
	setAttr ".RightShoulderMinRLimity" -45;
	setAttr ".RightShoulderMinRLimitz" -45;
	setAttr ".RightShoulderMaxRLimitx" 45;
	setAttr ".RightShoulderMaxRLimity" 45;
	setAttr ".RightShoulderMaxRLimitz" 45;
	setAttr ".NeckTy" 145;
	setAttr ".NeckMinRLimitx" -45;
	setAttr ".NeckMinRLimity" -45;
	setAttr ".NeckMinRLimitz" -45;
	setAttr ".NeckMaxRLimitx" 45;
	setAttr ".NeckMaxRLimity" 45;
	setAttr ".NeckMaxRLimitz" 45;
	setAttr ".LeftFingerBaseTx" 80.519743439999999;
	setAttr ".LeftFingerBaseTy" 147.08957459999999;
	setAttr ".LeftFingerBaseTz" 1.304684401;
	setAttr ".LeftFingerBaseRy" -0.0035633340000000005;
	setAttr ".RightFingerBaseTx" -80.519626680000002;
	setAttr ".RightFingerBaseTy" 147.0898718;
	setAttr ".RightFingerBaseTz" 1.305458317;
	setAttr ".RightFingerBaseRy" -2.0000646359999998;
	setAttr ".Spine1Ty" 119.66666666666667;
	setAttr ".Spine1MinRLimitx" -45;
	setAttr ".Spine1MinRLimity" -45;
	setAttr ".Spine1MinRLimitz" -45;
	setAttr ".Spine1MaxRLimitx" 45;
	setAttr ".Spine1MaxRLimity" 45;
	setAttr ".Spine1MaxRLimitz" 45;
	setAttr ".Spine2Ty" 132.33333333333334;
	setAttr ".Spine2MinRLimitx" -45;
	setAttr ".Spine2MinRLimity" -45;
	setAttr ".Spine2MinRLimitz" -45;
	setAttr ".Spine2MaxRLimitx" 45;
	setAttr ".Spine2MaxRLimity" 45;
	setAttr ".Spine2MaxRLimitz" 45;
	setAttr ".Spine3Ty" 119;
	setAttr ".Spine4Ty" 123;
	setAttr ".Spine5Ty" 127;
	setAttr ".Spine6Ty" 131;
	setAttr ".Spine7Ty" 135;
	setAttr ".Spine8Ty" 139;
	setAttr ".Spine9Ty" 143;
	setAttr ".Neck1Ty" 147;
	setAttr ".Neck2Ty" 149;
	setAttr ".Neck3Ty" 151;
	setAttr ".Neck4Ty" 153;
	setAttr ".Neck5Ty" 155;
	setAttr ".Neck6Ty" 157;
	setAttr ".Neck7Ty" 159;
	setAttr ".Neck8Ty" 161;
	setAttr ".Neck9Ty" 163;
	setAttr ".LeftUpLegRollTx" 8.9100008010000007;
	setAttr ".LeftUpLegRollTy" 70.997711179999996;
	setAttr ".LeftLegRollTx" 8.9100008010000007;
	setAttr ".LeftLegRollTy" 26.759407039999999;
	setAttr ".RightUpLegRollTx" -8.9100035169999998;
	setAttr ".RightUpLegRollTy" 70.997711179999996;
	setAttr ".RightUpLegRollRx" -0.0011371;
	setAttr ".RightLegRollTx" -8.9100025980000002;
	setAttr ".RightLegRollTy" 26.75940705;
	setAttr ".RightLegRollTz" 0.00043902399999999999;
	setAttr ".LeftArmRollTx" 32.968441489999996;
	setAttr ".LeftArmRollTy" 146.58868419999999;
	setAttr ".LeftForeArmRollTx" 61.340445039999999;
	setAttr ".LeftForeArmRollTy" 146.58868419999999;
	setAttr ".RightArmRollTx" -32.968521590000002;
	setAttr ".RightArmRollTy" 146.58898;
	setAttr ".RightForeArmRollTx" -61.340504160000002;
	setAttr ".RightForeArmRollTy" 146.58898;
	setAttr ".HipsTranslationTy" 100;
	setAttr ".LeftHandThumb1Tx" 76.058620990000009;
	setAttr ".LeftHandThumb1Ty" 145.79018170000001;
	setAttr ".LeftHandThumb1Tz" 4.2824339670000002;
	setAttr ".LeftHandThumb1Rz" 0.0036764100000000006;
	setAttr ".LeftHandThumb1Sx" 0.99999999999999989;
	setAttr ".LeftHandThumb1Sy" 0.99999999999999989;
	setAttr ".LeftHandThumb1JointOrientz" 0.011029230000000003;
	setAttr ".LeftHandThumb1MinRLimitx" -45;
	setAttr ".LeftHandThumb1MinRLimity" -45;
	setAttr ".LeftHandThumb1MinRLimitz" -45;
	setAttr ".LeftHandThumb1MaxRLimitx" 45;
	setAttr ".LeftHandThumb1MaxRLimity" 45;
	setAttr ".LeftHandThumb1MaxRLimitz" 45;
	setAttr ".LeftHandThumb2Tx" 78.571210930000007;
	setAttr ".LeftHandThumb2Ty" 145.25408229999999;
	setAttr ".LeftHandThumb2Tz" 4.9898882910000006;
	setAttr ".LeftHandThumb2Rz" -0.0010331440000000008;
	setAttr ".LeftHandThumb2Sx" 0.99999999999999989;
	setAttr ".LeftHandThumb2Sy" 0.99999999999999989;
	setAttr ".LeftHandThumb2JointOrientz" -0.0044116920000000009;
	setAttr ".LeftHandThumb2MinRLimitx" -45;
	setAttr ".LeftHandThumb2MinRLimity" -45;
	setAttr ".LeftHandThumb2MinRLimitz" -45;
	setAttr ".LeftHandThumb2MaxRLimitx" 45;
	setAttr ".LeftHandThumb2MaxRLimity" 45;
	setAttr ".LeftHandThumb2MaxRLimitz" 45;
	setAttr ".LeftHandThumb3Tx" 81.114351339999999;
	setAttr ".LeftHandThumb3Ty" 145.25406909999998;
	setAttr ".LeftHandThumb3Tz" 4.989897633;
	setAttr ".LeftHandThumb3Rz" 0.0014893099999999995;
	setAttr ".LeftHandThumb3Sx" 0.99999999999999989;
	setAttr ".LeftHandThumb3Sy" 0.99999999999999989;
	setAttr ".LeftHandThumb3JointOrientz" 0.0025224540000000004;
	setAttr ".LeftHandThumb3MinRLimitx" -45;
	setAttr ".LeftHandThumb3MinRLimity" -45;
	setAttr ".LeftHandThumb3MinRLimitz" -45;
	setAttr ".LeftHandThumb3MaxRLimitx" 45;
	setAttr ".LeftHandThumb3MaxRLimity" 45;
	setAttr ".LeftHandThumb3MaxRLimitz" 45;
	setAttr ".LeftHandThumb4Tx" 83.78109748;
	setAttr ".LeftHandThumb4Ty" 145.254072;
	setAttr ".LeftHandThumb4Tz" 4.9898894219999992;
	setAttr ".LeftHandThumb4Rz" -0.00297862;
	setAttr ".LeftHandThumb4JointOrientz" -0.0044679299999999993;
	setAttr ".LeftHandThumb4MinRLimitx" -45;
	setAttr ".LeftHandThumb4MinRLimity" -45;
	setAttr ".LeftHandThumb4MinRLimitz" -45;
	setAttr ".LeftHandThumb4MaxRLimitx" 45;
	setAttr ".LeftHandThumb4MaxRLimity" 45;
	setAttr ".LeftHandThumb4MaxRLimitz" 45;
	setAttr ".LeftHandIndex1Tx" 80.531840860000017;
	setAttr ".LeftHandIndex1Ty" 146.7884134;
	setAttr ".LeftHandIndex1Tz" 3.4716694160000001;
	setAttr ".LeftHandIndex1Ry" -1.9999999850000005;
	setAttr ".LeftHandIndex1Rz" 0.0033770690000000021;
	setAttr ".LeftHandIndex1Sx" 0.99999999999999989;
	setAttr ".LeftHandIndex1Sy" 0.99999999999999978;
	setAttr ".LeftHandIndex1Sz" 0.99999999999999989;
	setAttr ".LeftHandIndex1JointOrientz" 0.011029230000000003;
	setAttr ".LeftHandIndex1MinRLimitx" -45;
	setAttr ".LeftHandIndex1MinRLimity" -45;
	setAttr ".LeftHandIndex1MinRLimitz" -45;
	setAttr ".LeftHandIndex1MaxRLimitx" 45;
	setAttr ".LeftHandIndex1MaxRLimity" 45;
	setAttr ".LeftHandIndex1MaxRLimitz" 45;
	setAttr ".LeftHandIndex2Tx" 84.75459545999999;
	setAttr ".LeftHandIndex2Ty" 146.7883913;
	setAttr ".LeftHandIndex2Tz" 3.6188684349999996;
	setAttr ".LeftHandIndex2Rx" 7.9389331973930138e-05;
	setAttr ".LeftHandIndex2Ry" 7.9999999395497623;
	setAttr ".LeftHandIndex2Rz" 0.00046811425600050161;
	setAttr ".LeftHandIndex2Sy" 0.99999999999999978;
	setAttr ".LeftHandIndex2Sz" 0.99999999999996914;
	setAttr ".LeftHandIndex2JointOrientx" 3.9767686272416974e-05;
	setAttr ".LeftHandIndex2JointOrienty" 11.999999906916589;
	setAttr ".LeftHandIndex2JointOrientz" -0.0026199006522314512;
	setAttr ".LeftHandIndex2MinRLimitx" -45;
	setAttr ".LeftHandIndex2MinRLimity" -45;
	setAttr ".LeftHandIndex2MinRLimitz" -45;
	setAttr ".LeftHandIndex2MaxRLimitx" 45;
	setAttr ".LeftHandIndex2MaxRLimity" 45;
	setAttr ".LeftHandIndex2MaxRLimitz" 45;
	setAttr ".LeftHandIndex3Tx" 87.406920909999997;
	setAttr ".LeftHandIndex3Ty" 146.7883775;
	setAttr ".LeftHandIndex3Tz" 3.7113244149999987;
	setAttr ".LeftHandIndex3Rx" 0.00015974860091913891;
	setAttr ".LeftHandIndex3Ry" -11.999999908472555;
	setAttr ".LeftHandIndex3Rz" -0.0018192474217866535;
	setAttr ".LeftHandIndex3Sy" 0.99999999999999978;
	setAttr ".LeftHandIndex3JointOrientx" 0.00031182480137193966;
	setAttr ".LeftHandIndex3JointOrienty" -17.999999861621749;
	setAttr ".LeftHandIndex3JointOrientz" -0.0020221329458448675;
	setAttr ".LeftHandIndex3MinRLimitx" -45;
	setAttr ".LeftHandIndex3MinRLimity" -45;
	setAttr ".LeftHandIndex3MinRLimitz" -45;
	setAttr ".LeftHandIndex3MaxRLimitx" 45;
	setAttr ".LeftHandIndex3MaxRLimity" 45;
	setAttr ".LeftHandIndex3MaxRLimitz" 45;
	setAttr ".LeftHandIndex4Tx" 89.36395514000003;
	setAttr ".LeftHandIndex4Ty" 146.78836730000003;
	setAttr ".LeftHandIndex4Tz" 3.779543315000006;
	setAttr ".LeftHandIndex4Rx" 0.0001053024885678877;
	setAttr ".LeftHandIndex4Ry" 7.9999999391747494;
	setAttr ".LeftHandIndex4Rz" 0.0012065547564111747;
	setAttr ".LeftHandIndex4Sy" 0.99999999999999978;
	setAttr ".LeftHandIndex4JointOrientx" 0.00073387615628503857;
	setAttr ".LeftHandIndex4JointOrienty" 21.999999820320067;
	setAttr ".LeftHandIndex4JointOrientz" 0.0034761245573327409;
	setAttr ".LeftHandIndex4MinRLimitx" -45;
	setAttr ".LeftHandIndex4MinRLimity" -45;
	setAttr ".LeftHandIndex4MinRLimitz" -45;
	setAttr ".LeftHandIndex4MaxRLimitx" 45;
	setAttr ".LeftHandIndex4MaxRLimity" 45;
	setAttr ".LeftHandIndex4MaxRLimitz" 45;
	setAttr ".LeftHandMiddle1Tx" 80.519743500000018;
	setAttr ".LeftHandMiddle1Ty" 147.08957470000001;
	setAttr ".LeftHandMiddle1Tz" 1.3046843809999999;
	setAttr ".LeftHandMiddle1Ry" -0.0035633340000000018;
	setAttr ".LeftHandMiddle1Rz" 0.0036764100000000023;
	setAttr ".LeftHandMiddle1Sx" 0.99999999999999989;
	setAttr ".LeftHandMiddle1Sy" 0.99999999999999989;
	setAttr ".LeftHandMiddle1Sz" 0.99999999999999989;
	setAttr ".LeftHandMiddle1JointOrientz" 0.011029230000000003;
	setAttr ".LeftHandMiddle1MinRLimitx" -45;
	setAttr ".LeftHandMiddle1MinRLimity" -45;
	setAttr ".LeftHandMiddle1MinRLimitz" -45;
	setAttr ".LeftHandMiddle1MaxRLimitx" 45;
	setAttr ".LeftHandMiddle1MaxRLimity" 45;
	setAttr ".LeftHandMiddle1MaxRLimitz" 45;
	setAttr ".LeftHandMiddle2Tx" 85.382995179999995;
	setAttr ".LeftHandMiddle2Ty" 147.08957469999999;
	setAttr ".LeftHandMiddle2Tz" 1.3049868360000001;
	setAttr ".LeftHandMiddle2Ry" 0.014253335999706586;
	setAttr ".LeftHandMiddle2Rz" -0.00073528202986146364;
	setAttr ".LeftHandMiddle2Sy" 0.99999999999999978;
	setAttr ".LeftHandMiddle2Sz" 0.99999999999999989;
	setAttr ".LeftHandMiddle2JointOrientx" -2.7437157412159982e-07;
	setAttr ".LeftHandMiddle2JointOrienty" 0.021380003989143481;
	setAttr ".LeftHandMiddle2JointOrientz" -0.0044116921066480802;
	setAttr ".LeftHandMiddle2MinRLimitx" -45;
	setAttr ".LeftHandMiddle2MinRLimity" -45;
	setAttr ".LeftHandMiddle2MinRLimitz" -45;
	setAttr ".LeftHandMiddle2MaxRLimitx" 45;
	setAttr ".LeftHandMiddle2MaxRLimity" 45;
	setAttr ".LeftHandMiddle2MaxRLimitz" 45;
	setAttr ".LeftHandMiddle3Tx" 88.148231790000011;
	setAttr ".LeftHandMiddle3Ty" 147.08957470000004;
	setAttr ".LeftHandMiddle3Tz" 1.3051586189999997;
	setAttr ".LeftHandMiddle3Ry" -0.021380004000000018;
	setAttr ".LeftHandMiddle3Sy" 0.99999999999999978;
	setAttr ".LeftHandMiddle3JointOrientx" -4.5728601627035792e-07;
	setAttr ".LeftHandMiddle3JointOrienty" -0.032070005995011877;
	setAttr ".LeftHandMiddle3JointOrientz" 0.00073528226306528079;
	setAttr ".LeftHandMiddle3MinRLimitx" -45;
	setAttr ".LeftHandMiddle3MinRLimity" -45;
	setAttr ".LeftHandMiddle3MinRLimitz" -45;
	setAttr ".LeftHandMiddle3MaxRLimitx" 45;
	setAttr ".LeftHandMiddle3MaxRLimity" 45;
	setAttr ".LeftHandMiddle3MaxRLimitz" 45;
	setAttr ".LeftHandMiddle4Tx" 90.153863950000002;
	setAttr ".LeftHandMiddle4Ty" 147.08957469999996;
	setAttr ".LeftHandMiddle4Tz" 1.3052822150000001;
	setAttr ".LeftHandMiddle4Ry" 0.014253335999999998;
	setAttr ".LeftHandMiddle4Sy" 0.99999999999999978;
	setAttr ".LeftHandMiddle4JointOrientx" -4.5728612239275568e-07;
	setAttr ".LeftHandMiddle4JointOrienty" 0.039196674000000008;
	setAttr ".LeftHandMiddle4JointOrientz" -2.8439495905273179e-10;
	setAttr ".LeftHandMiddle4MinRLimitx" -45;
	setAttr ".LeftHandMiddle4MinRLimity" -45;
	setAttr ".LeftHandMiddle4MinRLimitz" -45;
	setAttr ".LeftHandMiddle4MaxRLimitx" 45;
	setAttr ".LeftHandMiddle4MaxRLimity" 45;
	setAttr ".LeftHandMiddle4MaxRLimitz" 45;
	setAttr ".LeftHandRing1Tx" 80.603623930000012;
	setAttr ".LeftHandRing1Ty" 146.96860380000004;
	setAttr ".LeftHandRing1Tz" -0.79315890899999997;
	setAttr ".LeftHandRing1Ry" -0.0035635290000000002;
	setAttr ".LeftHandRing1Rz" 0.0036764099999999967;
	setAttr ".LeftHandRing1Sx" 0.99999999999999989;
	setAttr ".LeftHandRing1Sy" 0.99999999999999989;
	setAttr ".LeftHandRing1JointOrientz" 0.011029230000000003;
	setAttr ".LeftHandRing1MinRLimitx" -45;
	setAttr ".LeftHandRing1MinRLimity" -45;
	setAttr ".LeftHandRing1MinRLimitz" -45;
	setAttr ".LeftHandRing1MaxRLimitx" 45;
	setAttr ".LeftHandRing1MaxRLimity" 45;
	setAttr ".LeftHandRing1MaxRLimitz" 45;
	setAttr ".LeftHandRing2Tx" 85.141382759999999;
	setAttr ".LeftHandRing2Ty" 146.96860380000001;
	setAttr ".LeftHandRing2Tz" -0.79315882000000015;
	setAttr ".LeftHandRing2Ry" 0.014254115999706567;
	setAttr ".LeftHandRing2Rz" -0.00073528202986473067;
	setAttr ".LeftHandRing2Sx" 0.99999999999999978;
	setAttr ".LeftHandRing2Sy" 0.99999999999999978;
	setAttr ".LeftHandRing2Sz" 0.99999999999999989;
	setAttr ".LeftHandRing2JointOrientx" -2.7438658884226412e-07;
	setAttr ".LeftHandRing2JointOrienty" 0.021381173989142875;
	setAttr ".LeftHandRing2JointOrientz" -0.0044116921066597444;
	setAttr ".LeftHandRing2MinRLimitx" -45;
	setAttr ".LeftHandRing2MinRLimity" -45;
	setAttr ".LeftHandRing2MinRLimitz" -45;
	setAttr ".LeftHandRing2MaxRLimitx" 45;
	setAttr ".LeftHandRing2MaxRLimity" 45;
	setAttr ".LeftHandRing2MaxRLimitz" 45;
	setAttr ".LeftHandRing3Tx" 87.445908619999983;
	setAttr ".LeftHandRing3Ty" 146.96860380000001;
	setAttr ".LeftHandRing3Tz" -0.79315893700000006;
	setAttr ".LeftHandRing3Ry" -0.021381173999999996;
	setAttr ".LeftHandRing3Sx" 0.99999999999999978;
	setAttr ".LeftHandRing3Sy" 0.99999999999999978;
	setAttr ".LeftHandRing3Sz" 0.99999999999999989;
	setAttr ".LeftHandRing3JointOrientx" -4.5731104081453454e-07;
	setAttr ".LeftHandRing3JointOrienty" -0.032071760995011578;
	setAttr ".LeftHandRing3JointOrientz" 0.00073528226309407222;
	setAttr ".LeftHandRing3MinRLimitx" -45;
	setAttr ".LeftHandRing3MinRLimity" -45;
	setAttr ".LeftHandRing3MinRLimitz" -45;
	setAttr ".LeftHandRing3MaxRLimitx" 45;
	setAttr ".LeftHandRing3MaxRLimity" 45;
	setAttr ".LeftHandRing3MaxRLimitz" 45;
	setAttr ".LeftHandRing4Tx" 89.369255980000005;
	setAttr ".LeftHandRing4Ty" 146.96860380000001;
	setAttr ".LeftHandRing4Tz" -0.79315975400000016;
	setAttr ".LeftHandRing4Ry" 0.01425411599999998;
	setAttr ".LeftHandRing4Sx" 0.99999999999999978;
	setAttr ".LeftHandRing4Sy" 0.99999999999999978;
	setAttr ".LeftHandRing4Sz" 0.99999999999999989;
	setAttr ".LeftHandRing4JointOrientx" -4.5731114695435592e-07;
	setAttr ".LeftHandRing4JointOrienty" 0.039198818999999982;
	setAttr ".LeftHandRing4JointOrientz" -2.8442608627698344e-10;
	setAttr ".LeftHandRing4MinRLimitx" -45;
	setAttr ".LeftHandRing4MinRLimity" -45;
	setAttr ".LeftHandRing4MinRLimitz" -45;
	setAttr ".LeftHandRing4MaxRLimitx" 45;
	setAttr ".LeftHandRing4MaxRLimity" 45;
	setAttr ".LeftHandRing4MaxRLimitz" 45;
	setAttr ".LeftHandPinky1Tx" 80.59213883000001;
	setAttr ".LeftHandPinky1Ty" 146.27565720000001;
	setAttr ".LeftHandPinky1Tz" -2.4903564650000001;
	setAttr ".LeftHandPinky1Rz" 0.0044394360000000015;
	setAttr ".LeftHandPinky1Sx" 0.99999999999999989;
	setAttr ".LeftHandPinky1Sy" 0.99999999999999989;
	setAttr ".LeftHandPinky1JointOrientz" 0.011029230000000003;
	setAttr ".LeftHandPinky1MinRLimitx" -45;
	setAttr ".LeftHandPinky1MinRLimity" -45;
	setAttr ".LeftHandPinky1MinRLimitz" -45;
	setAttr ".LeftHandPinky1MaxRLimitx" 45;
	setAttr ".LeftHandPinky1MaxRLimity" 45;
	setAttr ".LeftHandPinky1MaxRLimitz" 45;
	setAttr ".LeftHandPinky2Tx" 83.636238160000019;
	setAttr ".LeftHandPinky2Ty" 146.27569780000002;
	setAttr ".LeftHandPinky2Tz" -2.4903564649999996;
	setAttr ".LeftHandPinky2Rz" -0.0037873859999999985;
	setAttr ".LeftHandPinky2JointOrientz" -0.0089898479999999999;
	setAttr ".LeftHandPinky2MinRLimitx" -45;
	setAttr ".LeftHandPinky2MinRLimity" -45;
	setAttr ".LeftHandPinky2MinRLimitz" -45;
	setAttr ".LeftHandPinky2MaxRLimitx" 45;
	setAttr ".LeftHandPinky2MaxRLimity" 45;
	setAttr ".LeftHandPinky2MaxRLimitz" 45;
	setAttr ".LeftHandPinky3Tx" 85.610739650000014;
	setAttr ".LeftHandPinky3Ty" 146.27572409999999;
	setAttr ".LeftHandPinky3Tz" -2.4903566080000004;
	setAttr ".LeftHandPinky3Rz" 0.0045781559999999982;
	setAttr ".LeftHandPinky3JointOrientz" 0.0076025159999999958;
	setAttr ".LeftHandPinky3MinRLimitx" -45;
	setAttr ".LeftHandPinky3MinRLimity" -45;
	setAttr ".LeftHandPinky3MinRLimitz" -45;
	setAttr ".LeftHandPinky3MaxRLimitx" 45;
	setAttr ".LeftHandPinky3MaxRLimity" 45;
	setAttr ".LeftHandPinky3MaxRLimitz" 45;
	setAttr ".LeftHandPinky4Tx" 87.277354299999999;
	setAttr ".LeftHandPinky4Ty" 146.27574630000001;
	setAttr ".LeftHandPinky4Tz" -2.4903558170000002;
	setAttr ".LeftHandPinky4Rz" -0.0030521039999999986;
	setAttr ".LeftHandPinky4Sx" 0.99999999999999989;
	setAttr ".LeftHandPinky4Sy" 0.99999999999999989;
	setAttr ".LeftHandPinky4JointOrientz" -0.0083932859999999981;
	setAttr ".LeftHandPinky4MinRLimitx" -45;
	setAttr ".LeftHandPinky4MinRLimity" -45;
	setAttr ".LeftHandPinky4MinRLimitz" -45;
	setAttr ".LeftHandPinky4MaxRLimitx" 45;
	setAttr ".LeftHandPinky4MaxRLimity" 45;
	setAttr ".LeftHandPinky4MaxRLimitz" 45;
	setAttr ".LeftHandExtraFinger1Tx" 80.592138829999996;
	setAttr ".LeftHandExtraFinger1Ty" 146.7884134;
	setAttr ".LeftHandExtraFinger1Tz" -4.4903564649999996;
	setAttr ".LeftHandExtraFinger1Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger1Rz" -0.00029934100000000001;
	setAttr ".LeftHandExtraFinger2Tx" 82.636238160000005;
	setAttr ".LeftHandExtraFinger2Ty" 146.7883913;
	setAttr ".LeftHandExtraFinger2Tz" -4.4903564649999996;
	setAttr ".LeftHandExtraFinger2Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger2Rz" -0.00029934100000000001;
	setAttr ".LeftHandExtraFinger3Tx" 84.610739649999999;
	setAttr ".LeftHandExtraFinger3Ty" 146.7883775;
	setAttr ".LeftHandExtraFinger3Tz" -4.4903566079999999;
	setAttr ".LeftHandExtraFinger3Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger3Rz" -0.00029934100000000001;
	setAttr ".LeftHandExtraFinger4Tx" 86.277354299999999;
	setAttr ".LeftHandExtraFinger4Ty" 146.7883673;
	setAttr ".LeftHandExtraFinger4Tz" -4.4903558170000002;
	setAttr ".LeftHandExtraFinger4Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger4Rz" -0.00029934100000000001;
	setAttr ".RightHandThumb1Tx" -76.058242059999998;
	setAttr ".RightHandThumb1Ty" 145.7904806;
	setAttr ".RightHandThumb1Tz" 4.2828147379999999;
	setAttr ".RightHandThumb1Rz" -0.011591805000000004;
	setAttr ".RightHandThumb1Sx" 0.99999999999999978;
	setAttr ".RightHandThumb1Sy" 0.99999999999999978;
	setAttr ".RightHandThumb1JointOrientz" -0.034775415000000004;
	setAttr ".RightHandThumb1MinRLimitx" -45;
	setAttr ".RightHandThumb1MinRLimity" -45;
	setAttr ".RightHandThumb1MinRLimitz" -45;
	setAttr ".RightHandThumb1MaxRLimitx" 45;
	setAttr ".RightHandThumb1MaxRLimity" 45;
	setAttr ".RightHandThumb1MaxRLimitz" 45;
	setAttr ".RightHandThumb2Tx" -78.57076957000001;
	setAttr ".RightHandThumb2Ty" 145.25438170000004;
	setAttr ".RightHandThumb2Tz" 4.9904913879999997;
	setAttr ".RightHandThumb2Rz" 0.0017162750000000034;
	setAttr ".RightHandThumb2Sx" 0.99999999999999978;
	setAttr ".RightHandThumb2Sy" 0.99999999999999978;
	setAttr ".RightHandThumb2JointOrientz" 0.013910166000000003;
	setAttr ".RightHandThumb2MinRLimitx" -45;
	setAttr ".RightHandThumb2MinRLimity" -45;
	setAttr ".RightHandThumb2MinRLimitz" -45;
	setAttr ".RightHandThumb2MaxRLimitx" 45;
	setAttr ".RightHandThumb2MaxRLimity" 45;
	setAttr ".RightHandThumb2MaxRLimitz" 45;
	setAttr ".RightHandThumb3Tx" -81.112358930000013;
	setAttr ".RightHandThumb3Ty" 145.25440850000001;
	setAttr ".RightHandThumb3Tz" 5.0793117029999992;
	setAttr ".RightHandThumb3Rz" 0.0026189360000000001;
	setAttr ".RightHandThumb3Sx" 0.99999999999999989;
	setAttr ".RightHandThumb3Sy" 0.99999999999999989;
	setAttr ".RightHandThumb3JointOrientz" 0.0012941549999999965;
	setAttr ".RightHandThumb3MinRLimitx" -45;
	setAttr ".RightHandThumb3MinRLimity" -45;
	setAttr ".RightHandThumb3MinRLimitz" -45;
	setAttr ".RightHandThumb3MaxRLimitx" 45;
	setAttr ".RightHandThumb3MaxRLimity" 45;
	setAttr ".RightHandThumb3MaxRLimitz" 45;
	setAttr ".RightHandThumb4Tx" -83.777478689999981;
	setAttr ".RightHandThumb4Ty" 145.2544268;
	setAttr ".RightHandThumb4Tz" 5.1724490199999993;
	setAttr ".RightHandThumb4Rz" -0.0044548839999999975;
	setAttr ".RightHandThumb4Sx" 0.99999999999999978;
	setAttr ".RightHandThumb4Sy" 0.99999999999999978;
	setAttr ".RightHandThumb4JointOrientz" -0.0066823259999999989;
	setAttr ".RightHandThumb4MinRLimitx" -45;
	setAttr ".RightHandThumb4MinRLimity" -45;
	setAttr ".RightHandThumb4MinRLimitz" -45;
	setAttr ".RightHandThumb4MaxRLimitx" 45;
	setAttr ".RightHandThumb4MaxRLimity" 45;
	setAttr ".RightHandThumb4MaxRLimitz" 45;
	setAttr ".RightHandIndex1Tx" -80.531533929999995;
	setAttr ".RightHandIndex1Ty" 146.78871240000004;
	setAttr ".RightHandIndex1Tz" 3.4724442959999999;
	setAttr ".RightHandIndex1Ry" -2.0000646580000003;
	setAttr ".RightHandIndex1Rz" -0.011591805000000011;
	setAttr ".RightHandIndex1Sx" 0.99999999999999978;
	setAttr ".RightHandIndex1Sy" 0.99999999999999978;
	setAttr ".RightHandIndex1Sz" 0.99999999999999989;
	setAttr ".RightHandIndex1JointOrientz" -0.034775415000000004;
	setAttr ".RightHandIndex1MinRLimitx" -45;
	setAttr ".RightHandIndex1MinRLimity" -45;
	setAttr ".RightHandIndex1MinRLimitz" -45;
	setAttr ".RightHandIndex1MaxRLimitx" 45;
	setAttr ".RightHandIndex1MaxRLimity" 45;
	setAttr ".RightHandIndex1MaxRLimitz" 45;
	setAttr ".RightHandIndex2Tx" -84.754284149999989;
	setAttr ".RightHandIndex2Ty" 146.7887121;
	setAttr ".RightHandIndex2Tz" 3.3250925079999996;
	setAttr ".RightHandIndex2Rx" 8.170746952988914e-05;
	setAttr ".RightHandIndex2Ry" 8.0002586523559884;
	setAttr ".RightHandIndex2Rz" 0.0023283204729839732;
	setAttr ".RightHandIndex2Sx" 0.99999999999999978;
	setAttr ".RightHandIndex2Sy" 0.99999999999999978;
	setAttr ".RightHandIndex2JointOrientx" 0.00057893916151730137;
	setAttr ".RightHandIndex2JointOrienty" 12.000387886911755;
	setAttr ".RightHandIndex2JointOrientz" 0.014017828407258326;
	setAttr ".RightHandIndex2MinRLimitx" -45;
	setAttr ".RightHandIndex2MinRLimity" -45;
	setAttr ".RightHandIndex2MinRLimitz" -45;
	setAttr ".RightHandIndex2MaxRLimitx" 45;
	setAttr ".RightHandIndex2MaxRLimity" 45;
	setAttr ".RightHandIndex2MaxRLimitz" 45;
	setAttr ".RightHandIndex3Tx" -87.406606949999997;
	setAttr ".RightHandIndex3Ty" 146.78871179999999;
	setAttr ".RightHandIndex3Tz" 3.2325403670000012;
	setAttr ".RightHandIndex3Ry" -12.000387969999998;
	setAttr ".RightHandIndex3Sx" 0.99999999999999978;
	setAttr ".RightHandIndex3Sy" 0.99999999999999978;
	setAttr ".RightHandIndex3Sz" 0.99999999999999989;
	setAttr ".RightHandIndex3JointOrientx" 0.00025481484529355864;
	setAttr ".RightHandIndex3JointOrienty" -18.000581982957364;
	setAttr ".RightHandIndex3JointOrientz" -0.0023844045345728028;
	setAttr ".RightHandIndex3MinRLimitx" -45;
	setAttr ".RightHandIndex3MinRLimity" -45;
	setAttr ".RightHandIndex3MinRLimitz" -45;
	setAttr ".RightHandIndex3MaxRLimitx" 45;
	setAttr ".RightHandIndex3MaxRLimity" 45;
	setAttr ".RightHandIndex3MaxRLimitz" 45;
	setAttr ".RightHandIndex4Tx" -89.363639169999985;
	setAttr ".RightHandIndex4Ty" 146.78871169999999;
	setAttr ".RightHandIndex4Tz" 3.1642502150000045;
	setAttr ".RightHandIndex4Ry" 8.0002585659999941;
	setAttr ".RightHandIndex4Sx" 0.99999999999999989;
	setAttr ".RightHandIndex4Sy" 0.99999999999999978;
	setAttr ".RightHandIndex4JointOrientx" -3.0848417334584165e-18;
	setAttr ".RightHandIndex4JointOrienty" 22.000711171999988;
	setAttr ".RightHandIndex4JointOrientz" -4.1374294274114837e-19;
	setAttr ".RightHandIndex4MinRLimitx" -45;
	setAttr ".RightHandIndex4MinRLimity" -45;
	setAttr ".RightHandIndex4MinRLimitz" -45;
	setAttr ".RightHandIndex4MaxRLimitx" 45;
	setAttr ".RightHandIndex4MaxRLimity" 45;
	setAttr ".RightHandIndex4MaxRLimitz" 45;
	setAttr ".RightHandMiddle1Tx" -80.519627299999996;
	setAttr ".RightHandMiddle1Ty" 147.08987180000003;
	setAttr ".RightHandMiddle1Tz" 1.305458427;
	setAttr ".RightHandMiddle1Ry" -2.0000646580000003;
	setAttr ".RightHandMiddle1Rz" -0.011591805000000011;
	setAttr ".RightHandMiddle1Sx" 0.99999999999999978;
	setAttr ".RightHandMiddle1Sy" 0.99999999999999978;
	setAttr ".RightHandMiddle1Sz" 0.99999999999999989;
	setAttr ".RightHandMiddle1JointOrientz" -0.034775415000000004;
	setAttr ".RightHandMiddle1MinRLimitx" -45;
	setAttr ".RightHandMiddle1MinRLimity" -45;
	setAttr ".RightHandMiddle1MinRLimitz" -45;
	setAttr ".RightHandMiddle1MaxRLimitx" 45;
	setAttr ".RightHandMiddle1MaxRLimity" 45;
	setAttr ".RightHandMiddle1MaxRLimitz" 45;
	setAttr ".RightHandMiddle2Tx" -85.379921789999997;
	setAttr ".RightHandMiddle2Ty" 147.08987139999996;
	setAttr ".RightHandMiddle2Tz" 1.1358596750000003;
	setAttr ".RightHandMiddle2Rx" 8.170746952988914e-05;
	setAttr ".RightHandMiddle2Ry" 8.0002586523559884;
	setAttr ".RightHandMiddle2Rz" 0.0023283204729839732;
	setAttr ".RightHandMiddle2Sx" 0.99999999999999978;
	setAttr ".RightHandMiddle2Sy" 0.99999999999999978;
	setAttr ".RightHandMiddle2JointOrientx" 0.00057893916151730137;
	setAttr ".RightHandMiddle2JointOrienty" 12.000387886911755;
	setAttr ".RightHandMiddle2JointOrientz" 0.014017828407258326;
	setAttr ".RightHandMiddle2MinRLimitx" -45;
	setAttr ".RightHandMiddle2MinRLimity" -45;
	setAttr ".RightHandMiddle2MinRLimitz" -45;
	setAttr ".RightHandMiddle2MaxRLimitx" 45;
	setAttr ".RightHandMiddle2MaxRLimity" 45;
	setAttr ".RightHandMiddle2MaxRLimitz" 45;
	setAttr ".RightHandMiddle3Tx" -88.143476889999974;
	setAttr ".RightHandMiddle3Ty" 147.08987120000003;
	setAttr ".RightHandMiddle3Tz" 1.0394261129999987;
	setAttr ".RightHandMiddle3Ry" -12.000387969999998;
	setAttr ".RightHandMiddle3Sx" 0.99999999999999978;
	setAttr ".RightHandMiddle3Sy" 0.99999999999999978;
	setAttr ".RightHandMiddle3Sz" 0.99999999999999989;
	setAttr ".RightHandMiddle3JointOrientx" 0.00025481484529355864;
	setAttr ".RightHandMiddle3JointOrienty" -18.000581982957364;
	setAttr ".RightHandMiddle3JointOrientz" -0.0023844045345728028;
	setAttr ".RightHandMiddle3MinRLimitx" -45;
	setAttr ".RightHandMiddle3MinRLimity" -45;
	setAttr ".RightHandMiddle3MinRLimitz" -45;
	setAttr ".RightHandMiddle3MaxRLimitx" 45;
	setAttr ".RightHandMiddle3MaxRLimity" 45;
	setAttr ".RightHandMiddle3MaxRLimitz" 45;
	setAttr ".RightHandMiddle4Tx" -90.147889570000004;
	setAttr ".RightHandMiddle4Ty" 147.089871;
	setAttr ".RightHandMiddle4Tz" 0.96948263799999868;
	setAttr ".RightHandMiddle4Ry" 8.0002585659999941;
	setAttr ".RightHandMiddle4Sx" 0.99999999999999989;
	setAttr ".RightHandMiddle4Sy" 0.99999999999999978;
	setAttr ".RightHandMiddle4JointOrientx" -3.0848417334584165e-18;
	setAttr ".RightHandMiddle4JointOrienty" 22.000711171999988;
	setAttr ".RightHandMiddle4JointOrientz" -4.1374294274114837e-19;
	setAttr ".RightHandMiddle4MinRLimitx" -45;
	setAttr ".RightHandMiddle4MinRLimity" -45;
	setAttr ".RightHandMiddle4MinRLimitz" -45;
	setAttr ".RightHandMiddle4MaxRLimitx" 45;
	setAttr ".RightHandMiddle4MaxRLimity" 45;
	setAttr ".RightHandMiddle4MaxRLimitz" 45;
	setAttr ".RightHandRing1Tx" -80.603693699999994;
	setAttr ".RightHandRing1Ty" 146.968899;
	setAttr ".RightHandRing1Tz" -0.79237675600000002;
	setAttr ".RightHandRing1Ry" -2.0000646580000003;
	setAttr ".RightHandRing1Rz" -0.011591805000000011;
	setAttr ".RightHandRing1Sx" 0.99999999999999978;
	setAttr ".RightHandRing1Sy" 0.99999999999999978;
	setAttr ".RightHandRing1Sz" 0.99999999999999989;
	setAttr ".RightHandRing1JointOrientz" -0.034775415000000004;
	setAttr ".RightHandRing1MinRLimitx" -45;
	setAttr ".RightHandRing1MinRLimity" -45;
	setAttr ".RightHandRing1MinRLimitz" -45;
	setAttr ".RightHandRing1MaxRLimitx" 45;
	setAttr ".RightHandRing1MaxRLimity" 45;
	setAttr ".RightHandRing1MaxRLimitz" 45;
	setAttr ".RightHandRing2Tx" -85.138693309999979;
	setAttr ".RightHandRing2Ty" 146.96889860000002;
	setAttr ".RightHandRing2Tz" -0.9506244279999998;
	setAttr ".RightHandRing2Rx" 8.170746952988914e-05;
	setAttr ".RightHandRing2Ry" 8.0002586523559884;
	setAttr ".RightHandRing2Rz" 0.0023283204729839732;
	setAttr ".RightHandRing2Sx" 0.99999999999999978;
	setAttr ".RightHandRing2Sy" 0.99999999999999978;
	setAttr ".RightHandRing2JointOrientx" 0.00057893916151730137;
	setAttr ".RightHandRing2JointOrienty" 12.000387886911755;
	setAttr ".RightHandRing2JointOrientz" 0.014017828407258326;
	setAttr ".RightHandRing2MinRLimitx" -45;
	setAttr ".RightHandRing2MinRLimity" -45;
	setAttr ".RightHandRing2MinRLimitz" -45;
	setAttr ".RightHandRing2MaxRLimitx" 45;
	setAttr ".RightHandRing2MaxRLimity" 45;
	setAttr ".RightHandRing2MaxRLimitz" 45;
	setAttr ".RightHandRing3Tx" -87.441817880000002;
	setAttr ".RightHandRing3Ty" 146.96889840000003;
	setAttr ".RightHandRing3Tz" -1.0309913799999997;
	setAttr ".RightHandRing3Ry" -12.000387969999998;
	setAttr ".RightHandRing3Sx" 0.99999999999999978;
	setAttr ".RightHandRing3Sy" 0.99999999999999978;
	setAttr ".RightHandRing3Sz" 0.99999999999999989;
	setAttr ".RightHandRing3JointOrientx" 0.00025481484529355864;
	setAttr ".RightHandRing3JointOrienty" -18.000581982957364;
	setAttr ".RightHandRing3JointOrientz" -0.0023844045345728028;
	setAttr ".RightHandRing3MinRLimitx" -45;
	setAttr ".RightHandRing3MinRLimity" -45;
	setAttr ".RightHandRing3MinRLimitz" -45;
	setAttr ".RightHandRing3MaxRLimitx" 45;
	setAttr ".RightHandRing3MaxRLimity" 45;
	setAttr ".RightHandRing3MaxRLimitz" 45;
	setAttr ".RightHandRing4Tx" -89.363995799999984;
	setAttr ".RightHandRing4Ty" 146.96889830000001;
	setAttr ".RightHandRing4Tz" -1.098065296000001;
	setAttr ".RightHandRing4Ry" 8.0002585659999941;
	setAttr ".RightHandRing4Sx" 0.99999999999999989;
	setAttr ".RightHandRing4Sy" 0.99999999999999978;
	setAttr ".RightHandRing4JointOrientx" -3.0848417334584165e-18;
	setAttr ".RightHandRing4JointOrienty" 22.000711171999988;
	setAttr ".RightHandRing4JointOrientz" -4.1374294274114837e-19;
	setAttr ".RightHandRing4MinRLimitx" -45;
	setAttr ".RightHandRing4MinRLimity" -45;
	setAttr ".RightHandRing4MinRLimitz" -45;
	setAttr ".RightHandRing4MaxRLimitx" 45;
	setAttr ".RightHandRing4MaxRLimity" 45;
	setAttr ".RightHandRing4MaxRLimitz" 45;
	setAttr ".RightHandPinky1Tx" -80.592357370000002;
	setAttr ".RightHandPinky1Ty" 146.2759509;
	setAttr ".RightHandPinky1Tz" -2.4895741939999998;
	setAttr ".RightHandPinky1Ry" -2.0000646580000008;
	setAttr ".RightHandPinky1Rz" -0.010350589999999998;
	setAttr ".RightHandPinky1Sx" 0.99999999999999978;
	setAttr ".RightHandPinky1Sy" 0.99999999999999978;
	setAttr ".RightHandPinky1Sz" 0.99999999999999989;
	setAttr ".RightHandPinky1JointOrientz" -0.034775415000000004;
	setAttr ".RightHandPinky1MinRLimitx" -45;
	setAttr ".RightHandPinky1MinRLimity" -45;
	setAttr ".RightHandPinky1MinRLimitz" -45;
	setAttr ".RightHandPinky1MaxRLimitx" 45;
	setAttr ".RightHandPinky1MaxRLimity" 45;
	setAttr ".RightHandPinky1MaxRLimitz" 45;
	setAttr ".RightHandPinky2Tx" -83.638299989999979;
	setAttr ".RightHandPinky2Ty" 146.27588489999999;
	setAttr ".RightHandPinky2Tz" -2.5958615950000001;
	setAttr ".RightHandPinky2Rx" -0.00035494277400807212;
	setAttr ".RightHandPinky2Ry" 8.0002586452316287;
	setAttr ".RightHandPinky2Rz" -0.0026746514074187139;
	setAttr ".RightHandPinky2Sx" 0.99999999999999978;
	setAttr ".RightHandPinky2Sy" 0.99999999999999978;
	setAttr ".RightHandPinky2Sz" 0.99999999999995437;
	setAttr ".RightHandPinky2JointOrientx" -0.0003473165155227558;
	setAttr ".RightHandPinky2JointOrienty" 12.000387916518784;
	setAttr ".RightHandPinky2JointOrientz" 0.0064465962630108299;
	setAttr ".RightHandPinky2MinRLimitx" -45;
	setAttr ".RightHandPinky2MinRLimity" -45;
	setAttr ".RightHandPinky2MinRLimitz" -45;
	setAttr ".RightHandPinky2MaxRLimitx" 45;
	setAttr ".RightHandPinky2MaxRLimity" 45;
	setAttr ".RightHandPinky2MaxRLimitz" 45;
	setAttr ".RightHandPinky3Tx" -85.61399713000003;
	setAttr ".RightHandPinky3Ty" 146.27584210000001;
	setAttr ".RightHandPinky3Tz" -2.6648030449999962;
	setAttr ".RightHandPinky3Rx" -0.00066241850897411634;
	setAttr ".RightHandPinky3Ry" -12.000387943736966;
	setAttr ".RightHandPinky3Rz" 0.0075435008381052821;
	setAttr ".RightHandPinky3Sx" 0.99999999999999989;
	setAttr ".RightHandPinky3Sy" 0.99999999999999978;
	setAttr ".RightHandPinky3JointOrientx" -0.0013733125576394611;
	setAttr ".RightHandPinky3JointOrienty" -18.000581921549415;
	setAttr ".RightHandPinky3JointOrientz" 0.009136064439409123;
	setAttr ".RightHandPinky3MinRLimitx" -45;
	setAttr ".RightHandPinky3MinRLimity" -45;
	setAttr ".RightHandPinky3MinRLimitz" -45;
	setAttr ".RightHandPinky3MaxRLimitx" 45;
	setAttr ".RightHandPinky3MaxRLimity" 45;
	setAttr ".RightHandPinky3MaxRLimitz" 45;
	setAttr ".RightHandPinky4Tx" -87.28162098;
	setAttr ".RightHandPinky4Ty" 146.27580589999997;
	setAttr ".RightHandPinky4Tz" -2.7229943640000003;
	setAttr ".RightHandPinky4Rx" -0.00043665024183268584;
	setAttr ".RightHandPinky4Ry" 8.0002585518105107;
	setAttr ".RightHandPinky4Rz" -0.0050029718795694565;
	setAttr ".RightHandPinky4Sx" 0.99999999999999989;
	setAttr ".RightHandPinky4Sy" 0.99999999999999978;
	setAttr ".RightHandPinky4Sz" 1.0000000000000002;
	setAttr ".RightHandPinky4JointOrientx" -0.0030431224584647996;
	setAttr ".RightHandPinky4JointOrienty" 22.00071091959277;
	setAttr ".RightHandPinky4JointOrientz" -0.014413774206572399;
	setAttr ".RightHandPinky4MinRLimitx" -45;
	setAttr ".RightHandPinky4MinRLimity" -45;
	setAttr ".RightHandPinky4MinRLimitz" -45;
	setAttr ".RightHandPinky4MaxRLimitx" 45;
	setAttr ".RightHandPinky4MaxRLimity" 45;
	setAttr ".RightHandPinky4MaxRLimitz" 45;
	setAttr ".RightHandExtraFinger1Tx" -80.592357370000002;
	setAttr ".RightHandExtraFinger1Ty" 146.78871240000001;
	setAttr ".RightHandExtraFinger1Tz" -4.4895741940000002;
	setAttr ".RightHandExtraFinger1Ry" -2.0000646579999999;
	setAttr ".RightHandExtraFinger2Tx" -82.638299989999993;
	setAttr ".RightHandExtraFinger2Ty" 146.7887121;
	setAttr ".RightHandExtraFinger2Tz" -4.5958615949999997;
	setAttr ".RightHandExtraFinger2Ry" -2.0000646359999998;
	setAttr ".RightHandExtraFinger3Tx" -84.613997130000001;
	setAttr ".RightHandExtraFinger3Ty" 146.78871179999999;
	setAttr ".RightHandExtraFinger3Tz" -4.6648030450000002;
	setAttr ".RightHandExtraFinger3Ry" -2.0000646359999998;
	setAttr ".RightHandExtraFinger4Tx" -86.28162098;
	setAttr ".RightHandExtraFinger4Ty" 146.78871169999999;
	setAttr ".RightHandExtraFinger4Tz" -4.7229943639999998;
	setAttr ".RightHandExtraFinger4Ry" -2.0000646359999998;
	setAttr ".LeftFootThumb1Tx" 6.18422217;
	setAttr ".LeftFootThumb1Ty" 4.9992492679999998;
	setAttr ".LeftFootThumb1Tz" 1.930123209;
	setAttr ".LeftFootThumb2Tx" 4.551409713;
	setAttr ".LeftFootThumb2Ty" 2.6643834059999998;
	setAttr ".LeftFootThumb2Tz" 3.591937658;
	setAttr ".LeftFootThumb3Tx" 3.4619466889999999;
	setAttr ".LeftFootThumb3Ty" 1.8880788850000001;
	setAttr ".LeftFootThumb3Tz" 6.4001420700000002;
	setAttr ".LeftFootThumb4Tx" 3.4619466999999999;
	setAttr ".LeftFootThumb4Ty" 1.8880788550000001;
	setAttr ".LeftFootThumb4Tz" 9.6971958839999992;
	setAttr ".LeftFootIndex1Tx" 7.1105199680000002;
	setAttr ".LeftFootIndex1Ty" 1.888079117;
	setAttr ".LeftFootIndex1Tz" 12.9547209;
	setAttr ".LeftFootIndex2Tx" 7.1105199749999999;
	setAttr ".LeftFootIndex2Ty" 1.8880790999999999;
	setAttr ".LeftFootIndex2Tz" 14.82972745;
	setAttr ".LeftFootIndex3Tx" 7.1105199810000004;
	setAttr ".LeftFootIndex3Ty" 1.888079083;
	setAttr ".LeftFootIndex3Tz" 16.76314442;
	setAttr ".LeftFootIndex4Tx" 7.1105199880000001;
	setAttr ".LeftFootIndex4Ty" 1.8880790649999999;
	setAttr ".LeftFootIndex4Tz" 18.850666449999999;
	setAttr ".LeftFootMiddle1Tx" 8.9167242489999996;
	setAttr ".LeftFootMiddle1Ty" 1.888079163;
	setAttr ".LeftFootMiddle1Tz" 12.9547209;
	setAttr ".LeftFootMiddle2Tx" 8.9167242550000001;
	setAttr ".LeftFootMiddle2Ty" 1.888079147;
	setAttr ".LeftFootMiddle2Tz" 14.82860045;
	setAttr ".LeftFootMiddle3Tx" 8.9167242610000006;
	setAttr ".LeftFootMiddle3Ty" 1.888079131;
	setAttr ".LeftFootMiddle3Tz" 16.64971237;
	setAttr ".LeftFootMiddle4Tx" 8.9167242669999993;
	setAttr ".LeftFootMiddle4Ty" 1.8880791139999999;
	setAttr ".LeftFootMiddle4Tz" 18.565581959999999;
	setAttr ".LeftFootRing1Tx" 10.723903740000001;
	setAttr ".LeftFootRing1Ty" 1.888079211;
	setAttr ".LeftFootRing1Tz" 12.9547209;
	setAttr ".LeftFootRing2Tx" 10.723903740000001;
	setAttr ".LeftFootRing2Ty" 1.888079195;
	setAttr ".LeftFootRing2Tz" 14.71345226;
	setAttr ".LeftFootRing3Tx" 10.72390375;
	setAttr ".LeftFootRing3Ty" 1.8880791800000001;
	setAttr ".LeftFootRing3Tz" 16.472174209999999;
	setAttr ".LeftFootRing4Tx" 10.723903760000001;
	setAttr ".LeftFootRing4Ty" 1.8880791640000001;
	setAttr ".LeftFootRing4Tz" 18.27484922;
	setAttr ".LeftFootPinky1Tx" 12.52979668;
	setAttr ".LeftFootPinky1Ty" 1.888079257;
	setAttr ".LeftFootPinky1Tz" 12.9547209;
	setAttr ".LeftFootPinky2Tx" 12.52979669;
	setAttr ".LeftFootPinky2Ty" 1.8880792420000001;
	setAttr ".LeftFootPinky2Tz" 14.5796458;
	setAttr ".LeftFootPinky3Tx" 12.52979669;
	setAttr ".LeftFootPinky3Ty" 1.8880792289999999;
	setAttr ".LeftFootPinky3Tz" 16.143599309999999;
	setAttr ".LeftFootPinky4Tx" 12.5297967;
	setAttr ".LeftFootPinky4Ty" 1.8880792129999999;
	setAttr ".LeftFootPinky4Tz" 17.861196199999998;
	setAttr ".LeftFootExtraFinger1Tx" 5.0860939849999998;
	setAttr ".LeftFootExtraFinger1Ty" 1.888079254;
	setAttr ".LeftFootExtraFinger1Tz" 12.9547209;
	setAttr ".LeftFootExtraFinger2Tx" 5.0860939910000003;
	setAttr ".LeftFootExtraFinger2Ty" 1.888079236;
	setAttr ".LeftFootExtraFinger2Tz" 14.94401483;
	setAttr ".LeftFootExtraFinger3Tx" 5.0860939979999999;
	setAttr ".LeftFootExtraFinger3Ty" 1.8880792179999999;
	setAttr ".LeftFootExtraFinger3Tz" 16.99182682;
	setAttr ".LeftFootExtraFinger4Tx" 5.0860940049999996;
	setAttr ".LeftFootExtraFinger4Ty" 1.8880791990000001;
	setAttr ".LeftFootExtraFinger4Tz" 19.0793827;
	setAttr ".RightFootThumb1Tx" -6.180000014;
	setAttr ".RightFootThumb1Ty" 4.9992496019999999;
	setAttr ".RightFootThumb1Tz" 1.930123112;
	setAttr ".RightFootThumb2Tx" -4.5499999820000001;
	setAttr ".RightFootThumb2Ty" 2.6643838419999999;
	setAttr ".RightFootThumb2Tz" 3.5919375690000002;
	setAttr ".RightFootThumb3Tx" -3.4599999860000001;
	setAttr ".RightFootThumb3Ty" 1.888079335;
	setAttr ".RightFootThumb3Tz" 6.4001419850000003;
	setAttr ".RightFootThumb4Tx" -3.4599999860000001;
	setAttr ".RightFootThumb4Ty" 1.8880793090000001;
	setAttr ".RightFootThumb4Tz" 9.6971957989999993;
	setAttr ".RightFootIndex1Tx" -7.1099999839999999;
	setAttr ".RightFootIndex1Ty" 1.888079262;
	setAttr ".RightFootIndex1Tz" 12.95472064;
	setAttr ".RightFootIndex2Tx" -7.1099999839999999;
	setAttr ".RightFootIndex2Ty" 1.8880792479999999;
	setAttr ".RightFootIndex2Tz" 14.82972719;
	setAttr ".RightFootIndex3Tx" -7.1099999839999999;
	setAttr ".RightFootIndex3Ty" 1.8880792340000001;
	setAttr ".RightFootIndex3Tz" 16.76314416;
	setAttr ".RightFootIndex4Tx" -7.1099999839999999;
	setAttr ".RightFootIndex4Ty" 1.8880792179999999;
	setAttr ".RightFootIndex4Tz" 18.850666189999998;
	setAttr ".RightFootMiddle1Tx" -8.92;
	setAttr ".RightFootMiddle1Ty" 1.8880792049999999;
	setAttr ".RightFootMiddle1Tz" 12.954720630000001;
	setAttr ".RightFootMiddle2Tx" -8.92;
	setAttr ".RightFootMiddle2Ty" 1.8880791910000001;
	setAttr ".RightFootMiddle2Tz" 14.82860018;
	setAttr ".RightFootMiddle3Tx" -8.92;
	setAttr ".RightFootMiddle3Ty" 1.8880791770000001;
	setAttr ".RightFootMiddle3Tz" 16.649712099999999;
	setAttr ".RightFootMiddle4Tx" -8.92;
	setAttr ".RightFootMiddle4Ty" 1.8880791619999999;
	setAttr ".RightFootMiddle4Tz" 18.565581689999998;
	setAttr ".RightFootRing1Tx" -10.72;
	setAttr ".RightFootRing1Ty" 1.8880791610000001;
	setAttr ".RightFootRing1Tz" 12.95472062;
	setAttr ".RightFootRing2Tx" -10.72;
	setAttr ".RightFootRing2Ty" 1.888079147;
	setAttr ".RightFootRing2Tz" 14.713451989999999;
	setAttr ".RightFootRing3Tx" -10.72;
	setAttr ".RightFootRing3Ty" 1.888079134;
	setAttr ".RightFootRing3Tz" 16.472173940000001;
	setAttr ".RightFootRing4Tx" -10.72;
	setAttr ".RightFootRing4Ty" 1.88807912;
	setAttr ".RightFootRing4Tz" 18.274848949999999;
	setAttr ".RightFootPinky1Tx" -12.530000060000001;
	setAttr ".RightFootPinky1Ty" 1.8880791029999999;
	setAttr ".RightFootPinky1Tz" 12.95472062;
	setAttr ".RightFootPinky2Tx" -12.530000060000001;
	setAttr ".RightFootPinky2Ty" 1.888079091;
	setAttr ".RightFootPinky2Tz" 14.57964552;
	setAttr ".RightFootPinky3Tx" -12.530000060000001;
	setAttr ".RightFootPinky3Ty" 1.8880790789999999;
	setAttr ".RightFootPinky3Tz" 16.143599040000002;
	setAttr ".RightFootPinky4Tx" -12.530000060000001;
	setAttr ".RightFootPinky4Ty" 1.888079066;
	setAttr ".RightFootPinky4Tz" 17.86119592;
	setAttr ".RightFootExtraFinger1Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger1Ty" 1.8880791260000001;
	setAttr ".RightFootExtraFinger1Tz" 12.95472064;
	setAttr ".RightFootExtraFinger2Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger2Ty" 1.8880791109999999;
	setAttr ".RightFootExtraFinger2Tz" 14.944014579999999;
	setAttr ".RightFootExtraFinger3Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger3Ty" 1.888079096;
	setAttr ".RightFootExtraFinger3Tz" 16.99182656;
	setAttr ".RightFootExtraFinger4Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger4Ty" 1.88807908;
	setAttr ".RightFootExtraFinger4Tz" 19.079382450000001;
	setAttr ".LeftInHandThumbTx" 71.709864199999998;
	setAttr ".LeftInHandThumbTy" 146.58868419999999;
	setAttr ".LeftInHandIndexTx" 71.709864199999998;
	setAttr ".LeftInHandIndexTy" 146.58868419999999;
	setAttr ".LeftInHandMiddleTx" 71.709864199999998;
	setAttr ".LeftInHandMiddleTy" 146.58868419999999;
	setAttr ".LeftInHandRingTx" 71.709864199999998;
	setAttr ".LeftInHandRingTy" 146.58868419999999;
	setAttr ".LeftInHandPinkyTx" 71.709864199999998;
	setAttr ".LeftInHandPinkyTy" 146.58868419999999;
	setAttr ".LeftInHandExtraFingerTx" 71.709864199999998;
	setAttr ".LeftInHandExtraFingerTy" 146.58868419999999;
	setAttr ".RightInHandThumbTx" -71.709861489999994;
	setAttr ".RightInHandThumbTy" 146.58897870000001;
	setAttr ".RightInHandIndexTx" -71.709861489999994;
	setAttr ".RightInHandIndexTy" 146.58897870000001;
	setAttr ".RightInHandMiddleTx" -71.709861489999994;
	setAttr ".RightInHandMiddleTy" 146.58897870000001;
	setAttr ".RightInHandRingTx" -71.709861489999994;
	setAttr ".RightInHandRingTy" 146.58897870000001;
	setAttr ".RightInHandPinkyTx" -71.709861489999994;
	setAttr ".RightInHandPinkyTy" 146.58897870000001;
	setAttr ".RightInHandExtraFingerTx" -71.709861489999994;
	setAttr ".RightInHandExtraFingerTy" 146.58897870000001;
	setAttr ".LeftInFootThumbTx" 8.9100008010000007;
	setAttr ".LeftInFootThumbTy" 8.15039625;
	setAttr ".LeftInFootIndexTx" 8.9100008010000007;
	setAttr ".LeftInFootIndexTy" 8.1503963469999992;
	setAttr ".LeftInFootMiddleTx" 8.9100008010000007;
	setAttr ".LeftInFootMiddleTy" 8.1503963469999992;
	setAttr ".LeftInFootRingTx" 8.9100008010000007;
	setAttr ".LeftInFootRingTy" 8.1503963469999992;
	setAttr ".LeftInFootPinkyTx" 8.9100008010000007;
	setAttr ".LeftInFootPinkyTy" 8.1503963469999992;
	setAttr ".LeftInFootExtraFingerTx" 8.9100008010000007;
	setAttr ".LeftInFootExtraFingerTy" 8.1503963469999992;
	setAttr ".RightInFootThumbTx" -8.9100025980000002;
	setAttr ".RightInFootThumbTy" 8.1503963929999994;
	setAttr ".RightInFootThumbTz" 0.00043882099999999999;
	setAttr ".RightInFootIndexTx" -8.9100026190000001;
	setAttr ".RightInFootIndexTy" 8.1503963939999995;
	setAttr ".RightInFootIndexTz" 0.00043882099999999999;
	setAttr ".RightInFootMiddleTx" -8.9100026190000001;
	setAttr ".RightInFootMiddleTy" 8.1503963939999995;
	setAttr ".RightInFootMiddleTz" 0.00043882099999999999;
	setAttr ".RightInFootRingTx" -8.9100026190000001;
	setAttr ".RightInFootRingTy" 8.1503963939999995;
	setAttr ".RightInFootRingTz" 0.00043882099999999999;
	setAttr ".RightInFootPinkyTx" -8.9100026190000001;
	setAttr ".RightInFootPinkyTy" 8.1503963939999995;
	setAttr ".RightInFootPinkyTz" 0.00043882099999999999;
	setAttr ".RightInFootExtraFingerTx" -8.9100026190000001;
	setAttr ".RightInFootExtraFingerTy" 8.1503963939999995;
	setAttr ".RightInFootExtraFingerTz" 0.00043882099999999999;
	setAttr ".LeftShoulderExtraTx" 12.353625535000001;
	setAttr ".LeftShoulderExtraTy" 146.58868419999999;
	setAttr ".RightShoulderExtraTx" -12.353637216499999;
	setAttr ".RightShoulderExtraTy" 146.58898;
createNode HIKProperty2State -n "HIKproperties1";
	rename -uid "747C7A16-4011-66BA-E8B0-51A22208B35F";
	setAttr ".ParamLeafLeftUpLegRoll1Mode" 0;
	setAttr ".ParamLeafLeftUpLegRoll1" 0;
	setAttr ".ParamLeafLeftLegRoll1Mode" 0;
	setAttr ".ParamLeafLeftLegRoll1" 0;
	setAttr ".ParamLeafRightUpLegRoll1Mode" 0;
	setAttr ".ParamLeafRightUpLegRoll1" 0;
	setAttr ".ParamLeafRightLegRoll1Mode" 0;
	setAttr ".ParamLeafRightLegRoll1" 0;
	setAttr ".ParamLeafLeftArmRoll1Mode" 0;
	setAttr ".ParamLeafLeftArmRoll1" 0;
	setAttr ".ParamLeafLeftForeArmRoll1Mode" 0;
	setAttr ".ParamLeafLeftForeArmRoll1" 0;
	setAttr ".ParamLeafRightArmRoll1Mode" 0;
	setAttr ".ParamLeafRightArmRoll1" 0;
	setAttr ".ParamLeafRightForeArmRoll1Mode" 0;
	setAttr ".ParamLeafRightForeArmRoll1" 0;
	setAttr ".ParamLeafLeftUpLegRoll2Mode" 0;
	setAttr ".ParamLeafLeftUpLegRoll2" 0;
	setAttr ".ParamLeafLeftLegRoll2Mode" 0;
	setAttr ".ParamLeafLeftLegRoll2" 0;
	setAttr ".ParamLeafRightUpLegRoll2Mode" 0;
	setAttr ".ParamLeafRightUpLegRoll2" 0;
	setAttr ".ParamLeafRightLegRoll2Mode" 0;
	setAttr ".ParamLeafRightLegRoll2" 0;
	setAttr ".ParamLeafLeftArmRoll2Mode" 0;
	setAttr ".ParamLeafLeftArmRoll2" 0;
	setAttr ".ParamLeafLeftForeArmRoll2Mode" 0;
	setAttr ".ParamLeafLeftForeArmRoll2" 0;
	setAttr ".ParamLeafRightArmRoll2Mode" 0;
	setAttr ".ParamLeafRightArmRoll2" 0;
	setAttr ".ParamLeafRightForeArmRoll2Mode" 0;
	setAttr ".ParamLeafRightForeArmRoll2" 0;
	setAttr ".ParamLeafLeftUpLegRoll3Mode" 0;
	setAttr ".ParamLeafLeftUpLegRoll3" 0;
	setAttr ".ParamLeafLeftLegRoll3Mode" 0;
	setAttr ".ParamLeafLeftLegRoll3" 0;
	setAttr ".ParamLeafRightUpLegRoll3Mode" 0;
	setAttr ".ParamLeafRightUpLegRoll3" 0;
	setAttr ".ParamLeafRightLegRoll3Mode" 0;
	setAttr ".ParamLeafRightLegRoll3" 0;
	setAttr ".ParamLeafLeftArmRoll3Mode" 0;
	setAttr ".ParamLeafLeftArmRoll3" 0;
	setAttr ".ParamLeafLeftForeArmRoll3Mode" 0;
	setAttr ".ParamLeafLeftForeArmRoll3" 0;
	setAttr ".ParamLeafRightArmRoll3Mode" 0;
	setAttr ".ParamLeafRightArmRoll3" 0;
	setAttr ".ParamLeafRightForeArmRoll3Mode" 0;
	setAttr ".ParamLeafRightForeArmRoll3" 0;
	setAttr ".ParamLeafLeftUpLegRoll4Mode" 0;
	setAttr ".ParamLeafLeftUpLegRoll4" 0;
	setAttr ".ParamLeafLeftLegRoll4Mode" 0;
	setAttr ".ParamLeafLeftLegRoll4" 0;
	setAttr ".ParamLeafRightUpLegRoll4Mode" 0;
	setAttr ".ParamLeafRightUpLegRoll4" 0;
	setAttr ".ParamLeafRightLegRoll4Mode" 0;
	setAttr ".ParamLeafRightLegRoll4" 0;
	setAttr ".ParamLeafLeftArmRoll4Mode" 0;
	setAttr ".ParamLeafLeftArmRoll4" 0;
	setAttr ".ParamLeafLeftForeArmRoll4Mode" 0;
	setAttr ".ParamLeafLeftForeArmRoll4" 0;
	setAttr ".ParamLeafRightArmRoll4Mode" 0;
	setAttr ".ParamLeafRightArmRoll4" 0;
	setAttr ".ParamLeafRightForeArmRoll4Mode" 0;
	setAttr ".ParamLeafRightForeArmRoll4" 0;
	setAttr ".ParamLeafLeftUpLegRoll5Mode" 0;
	setAttr ".ParamLeafLeftUpLegRoll5" 0;
	setAttr ".ParamLeafLeftLegRoll5Mode" 0;
	setAttr ".ParamLeafLeftLegRoll5" 0;
	setAttr ".ParamLeafRightUpLegRoll5Mode" 0;
	setAttr ".ParamLeafRightUpLegRoll5" 0;
	setAttr ".ParamLeafRightLegRoll5Mode" 0;
	setAttr ".ParamLeafRightLegRoll5" 0;
	setAttr ".ParamLeafLeftArmRoll5Mode" 0;
	setAttr ".ParamLeafLeftArmRoll5" 0;
	setAttr ".ParamLeafLeftForeArmRoll5Mode" 0;
	setAttr ".ParamLeafLeftForeArmRoll5" 0;
	setAttr ".ParamLeafRightArmRoll5Mode" 0;
	setAttr ".ParamLeafRightArmRoll5" 0;
	setAttr ".ParamLeafRightForeArmRoll5Mode" 0;
	setAttr ".ParamLeafRightForeArmRoll5" 0;
createNode HIKSkeletonGeneratorNode -n "HIKSkeletonGeneratorNode1";
	rename -uid "306B5AB0-4411-039C-ED7E-FB96C3A0A414";
	setAttr ".ihi" 0;
	setAttr ".WantIndexFinger" yes;
	setAttr ".WantMiddleFinger" yes;
	setAttr ".WantRingFinger" yes;
	setAttr ".WantPinkyFinger" yes;
	setAttr ".WantThumb" yes;
	setAttr ".WantToeBase" yes;
	setAttr ".HipsTy" 100;
	setAttr ".LeftUpLegTx" 8.9100008010000007;
	setAttr ".LeftUpLegTy" 93.729999539999994;
	setAttr ".LeftLegTx" 8.9100008010000007;
	setAttr ".LeftLegTy" 48.851354600000001;
	setAttr ".LeftFootTx" 8.9100008010000007;
	setAttr ".LeftFootTy" 8.1503963469999992;
	setAttr ".RightUpLegTx" -8.9100008010000007;
	setAttr ".RightUpLegTy" 93.729999539999994;
	setAttr ".RightLegTx" -8.9100035169999998;
	setAttr ".RightLegTy" 48.851354600000001;
	setAttr ".RightLegTz" 0.00043902399999999999;
	setAttr ".RightFootTx" -8.9100025980000002;
	setAttr ".RightFootTy" 8.1503963509999995;
	setAttr ".RightFootTz" 0.00043902399999999999;
	setAttr ".RightFootRy" -0.0048003860000000002;
	setAttr ".SpineTy" 107;
	setAttr ".LeftArmTx" 17.707251070000002;
	setAttr ".LeftArmTy" 146.58868419999999;
	setAttr ".LeftForeArmTx" 45.012716769999997;
	setAttr ".LeftForeArmTy" 146.58868419999999;
	setAttr ".LeftHandTx" 71.709864139999993;
	setAttr ".LeftHandTy" 146.58868419999999;
	setAttr ".RightArmTx" -17.707274909999999;
	setAttr ".RightArmTy" 146.58898;
	setAttr ".RightForeArmTx" -45.012873159999998;
	setAttr ".RightForeArmTy" 146.58898;
	setAttr ".RightHandTx" -71.709861270000005;
	setAttr ".RightHandTy" 146.58897870000001;
	setAttr ".HeadTy" 165;
	setAttr ".LeftToeBaseTx" 8.9100092279999998;
	setAttr ".LeftToeBaseTy" 1.8880791539999999;
	setAttr ".LeftToeBaseTz" 12.9547209;
	setAttr ".RightToeBaseTx" -8.9110879789999995;
	setAttr ".RightToeBaseTy" 1.888079171;
	setAttr ".RightToeBaseTz" 12.95518809;
	setAttr ".RightToeBaseRx" 0.0029125930000000002;
	setAttr ".RightToeBaseRy" -0.0048003860000000002;
	setAttr ".LeftShoulderTx" 7.0000004770000004;
	setAttr ".LeftShoulderTy" 146.58854679999999;
	setAttr ".LeftShoulderRz" 0.00073528199999999997;
	setAttr ".RightShoulderTx" -6.9999995229999996;
	setAttr ".RightShoulderTy" 146.58854679999999;
	setAttr ".RightShoulderRz" -0.0023183610000000001;
	setAttr ".NeckTy" 145;
	setAttr ".LeftFingerBaseTx" 80.519743439999999;
	setAttr ".LeftFingerBaseTy" 147.08957459999999;
	setAttr ".LeftFingerBaseTz" 1.304684401;
	setAttr ".LeftFingerBaseRy" -0.0035633340000000005;
	setAttr ".RightFingerBaseTx" -80.519626680000002;
	setAttr ".RightFingerBaseTy" 147.0898718;
	setAttr ".RightFingerBaseTz" 1.305458317;
	setAttr ".RightFingerBaseRy" -2.0000646359999998;
	setAttr ".Spine1Ty" 111;
	setAttr ".Spine2Ty" 115;
	setAttr ".Spine3Ty" 119;
	setAttr ".Spine4Ty" 123;
	setAttr ".Spine5Ty" 127;
	setAttr ".Spine6Ty" 131;
	setAttr ".Spine7Ty" 135;
	setAttr ".Spine8Ty" 139;
	setAttr ".Spine9Ty" 143;
	setAttr ".Neck1Ty" 147;
	setAttr ".Neck2Ty" 149;
	setAttr ".Neck3Ty" 151;
	setAttr ".Neck4Ty" 153;
	setAttr ".Neck5Ty" 155;
	setAttr ".Neck6Ty" 157;
	setAttr ".Neck7Ty" 159;
	setAttr ".Neck8Ty" 161;
	setAttr ".Neck9Ty" 163;
	setAttr ".LeftUpLegRollTx" 8.9100008010000007;
	setAttr ".LeftUpLegRollTy" 70.997711179999996;
	setAttr ".LeftLegRollTx" 8.9100008010000007;
	setAttr ".LeftLegRollTy" 26.759407039999999;
	setAttr ".RightUpLegRollTx" -8.9100035169999998;
	setAttr ".RightUpLegRollTy" 70.997711179999996;
	setAttr ".RightUpLegRollRx" -0.0011371;
	setAttr ".RightLegRollTx" -8.9100025980000002;
	setAttr ".RightLegRollTy" 26.75940705;
	setAttr ".RightLegRollTz" 0.00043902399999999999;
	setAttr ".LeftArmRollTx" 32.968441489999996;
	setAttr ".LeftArmRollTy" 146.58868419999999;
	setAttr ".LeftForeArmRollTx" 61.340445039999999;
	setAttr ".LeftForeArmRollTy" 146.58868419999999;
	setAttr ".RightArmRollTx" -32.968521590000002;
	setAttr ".RightArmRollTy" 146.58898;
	setAttr ".RightForeArmRollTx" -61.340504160000002;
	setAttr ".RightForeArmRollTy" 146.58898;
	setAttr ".HipsTranslationTy" 100;
	setAttr ".LeftHandThumb1Tx" 76.058620989999994;
	setAttr ".LeftHandThumb1Ty" 145.79018170000001;
	setAttr ".LeftHandThumb1Tz" 4.2824339670000002;
	setAttr ".LeftHandThumb2Tx" 78.571210930000007;
	setAttr ".LeftHandThumb2Ty" 145.25408229999999;
	setAttr ".LeftHandThumb2Tz" 4.9898882909999998;
	setAttr ".LeftHandThumb2Rz" -0.00029786199999999997;
	setAttr ".LeftHandThumb3Tx" 81.114351339999999;
	setAttr ".LeftHandThumb3Ty" 145.25406910000001;
	setAttr ".LeftHandThumb3Tz" 4.989897633;
	setAttr ".LeftHandThumb4Tx" 83.78109748;
	setAttr ".LeftHandThumb4Ty" 145.254072;
	setAttr ".LeftHandThumb4Tz" 4.9898894220000001;
	setAttr ".LeftHandIndex1Tx" 80.531840860000003;
	setAttr ".LeftHandIndex1Ty" 146.7884134;
	setAttr ".LeftHandIndex1Tz" 3.4716694160000001;
	setAttr ".LeftHandIndex1Ry" -1.9999999850000001;
	setAttr ".LeftHandIndex1Rz" -0.00029934100000000001;
	setAttr ".LeftHandIndex2Tx" 84.754595460000004;
	setAttr ".LeftHandIndex2Ty" 146.7883913;
	setAttr ".LeftHandIndex2Tz" 3.618868435;
	setAttr ".LeftHandIndex2Ry" -1.9999999850000001;
	setAttr ".LeftHandIndex2Rz" -0.00029934100000000001;
	setAttr ".LeftHandIndex3Tx" 87.406920909999997;
	setAttr ".LeftHandIndex3Ty" 146.7883775;
	setAttr ".LeftHandIndex3Tz" 3.711324415;
	setAttr ".LeftHandIndex3Ry" -1.9999999850000001;
	setAttr ".LeftHandIndex3Rz" -0.00029934100000000001;
	setAttr ".LeftHandIndex4Tx" 89.363955140000002;
	setAttr ".LeftHandIndex4Ty" 146.7883673;
	setAttr ".LeftHandIndex4Tz" 3.7795433150000002;
	setAttr ".LeftHandIndex4Ry" -1.9999999850000001;
	setAttr ".LeftHandIndex4Rz" -0.00029934100000000001;
	setAttr ".LeftHandMiddle1Tx" 80.519743500000004;
	setAttr ".LeftHandMiddle1Ty" 147.08957469999999;
	setAttr ".LeftHandMiddle1Tz" 1.3046843809999999;
	setAttr ".LeftHandMiddle1Ry" -0.0035633340000000005;
	setAttr ".LeftHandMiddle2Tx" 85.382995179999995;
	setAttr ".LeftHandMiddle2Ty" 147.08957469999999;
	setAttr ".LeftHandMiddle2Tz" 1.3049868360000001;
	setAttr ".LeftHandMiddle2Ry" -0.0035633340000000005;
	setAttr ".LeftHandMiddle3Tx" 88.148231789999997;
	setAttr ".LeftHandMiddle3Ty" 147.08957469999999;
	setAttr ".LeftHandMiddle3Tz" 1.305158619;
	setAttr ".LeftHandMiddle3Ry" -0.0035633340000000005;
	setAttr ".LeftHandMiddle4Tx" 90.153863950000002;
	setAttr ".LeftHandMiddle4Ty" 147.08957469999999;
	setAttr ".LeftHandMiddle4Tz" 1.3052822150000001;
	setAttr ".LeftHandMiddle4Ry" -0.0035633340000000005;
	setAttr ".LeftHandRing1Tx" 80.603623929999998;
	setAttr ".LeftHandRing1Ty" 146.96860380000001;
	setAttr ".LeftHandRing1Tz" -0.79315890899999997;
	setAttr ".LeftHandRing1Ry" -0.0035635290000000002;
	setAttr ".LeftHandRing2Tx" 85.141382759999999;
	setAttr ".LeftHandRing2Ty" 146.96860380000001;
	setAttr ".LeftHandRing2Tz" -0.79315882000000004;
	setAttr ".LeftHandRing2Ry" -0.0035635290000000002;
	setAttr ".LeftHandRing3Tx" 87.445908619999997;
	setAttr ".LeftHandRing3Ty" 146.96860380000001;
	setAttr ".LeftHandRing3Tz" -0.79315893699999995;
	setAttr ".LeftHandRing3Ry" -0.0035635290000000002;
	setAttr ".LeftHandRing4Tx" 89.369255980000005;
	setAttr ".LeftHandRing4Ty" 146.96860380000001;
	setAttr ".LeftHandRing4Tz" -0.79315975400000005;
	setAttr ".LeftHandRing4Ry" -0.0035635290000000002;
	setAttr ".LeftHandPinky1Tx" 80.592138829999996;
	setAttr ".LeftHandPinky1Ty" 146.27565720000001;
	setAttr ".LeftHandPinky1Tz" -2.4903564650000001;
	setAttr ".LeftHandPinky1Rz" 0.00076302599999999998;
	setAttr ".LeftHandPinky2Tx" 83.636238160000005;
	setAttr ".LeftHandPinky2Ty" 146.27569779999999;
	setAttr ".LeftHandPinky2Tz" -2.4903564650000001;
	setAttr ".LeftHandPinky2Rz" 0.00076302599999999998;
	setAttr ".LeftHandPinky3Tx" 85.610739649999999;
	setAttr ".LeftHandPinky3Ty" 146.27572409999999;
	setAttr ".LeftHandPinky3Tz" -2.4903566079999999;
	setAttr ".LeftHandPinky3Rz" 0.00076302599999999998;
	setAttr ".LeftHandPinky4Tx" 87.277354299999999;
	setAttr ".LeftHandPinky4Ty" 146.27574630000001;
	setAttr ".LeftHandPinky4Tz" -2.4903558170000002;
	setAttr ".LeftHandPinky4Rz" 0.00076302599999999998;
	setAttr ".LeftHandExtraFinger1Tx" 80.592138829999996;
	setAttr ".LeftHandExtraFinger1Ty" 146.7884134;
	setAttr ".LeftHandExtraFinger1Tz" -4.4903564649999996;
	setAttr ".LeftHandExtraFinger1Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger1Rz" -0.00029934100000000001;
	setAttr ".LeftHandExtraFinger2Tx" 82.636238160000005;
	setAttr ".LeftHandExtraFinger2Ty" 146.7883913;
	setAttr ".LeftHandExtraFinger2Tz" -4.4903564649999996;
	setAttr ".LeftHandExtraFinger2Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger2Rz" -0.00029934100000000001;
	setAttr ".LeftHandExtraFinger3Tx" 84.610739649999999;
	setAttr ".LeftHandExtraFinger3Ty" 146.7883775;
	setAttr ".LeftHandExtraFinger3Tz" -4.4903566079999999;
	setAttr ".LeftHandExtraFinger3Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger3Rz" -0.00029934100000000001;
	setAttr ".LeftHandExtraFinger4Tx" 86.277354299999999;
	setAttr ".LeftHandExtraFinger4Ty" 146.7883673;
	setAttr ".LeftHandExtraFinger4Tz" -4.4903558170000002;
	setAttr ".LeftHandExtraFinger4Ry" -1.9999999850000001;
	setAttr ".LeftHandExtraFinger4Rz" -0.00029934100000000001;
	setAttr ".RightHandThumb1Tx" -76.058242059999998;
	setAttr ".RightHandThumb1Ty" 145.7904806;
	setAttr ".RightHandThumb1Tz" 4.2828147379999999;
	setAttr ".RightHandThumb2Tx" -78.570769569999996;
	setAttr ".RightHandThumb2Ty" 145.25438170000001;
	setAttr ".RightHandThumb2Tz" 4.9904913879999997;
	setAttr ".RightHandThumb2Rz" -0.00060208600000000005;
	setAttr ".RightHandThumb3Tx" -81.112358929999999;
	setAttr ".RightHandThumb3Ty" 145.25440850000001;
	setAttr ".RightHandThumb3Tz" 5.0793117030000001;
	setAttr ".RightHandThumb3Rz" -0.00039149399999999999;
	setAttr ".RightHandThumb4Tx" -83.777478689999995;
	setAttr ".RightHandThumb4Ty" 145.2544268;
	setAttr ".RightHandThumb4Tz" 5.1724490200000002;
	setAttr ".RightHandThumb4Rz" -0.00039149399999999999;
	setAttr ".RightHandIndex1Tx" -80.531533929999995;
	setAttr ".RightHandIndex1Ty" 146.78871240000001;
	setAttr ".RightHandIndex1Tz" 3.4724442959999999;
	setAttr ".RightHandIndex1Ry" -2.0000646579999999;
	setAttr ".RightHandIndex2Tx" -84.754284150000004;
	setAttr ".RightHandIndex2Ty" 146.7887121;
	setAttr ".RightHandIndex2Tz" 3.325092508;
	setAttr ".RightHandIndex2Ry" -2.0000646359999998;
	setAttr ".RightHandIndex3Tx" -87.406606949999997;
	setAttr ".RightHandIndex3Ty" 146.78871179999999;
	setAttr ".RightHandIndex3Tz" 3.2325403669999999;
	setAttr ".RightHandIndex3Ry" -2.0000646359999998;
	setAttr ".RightHandIndex4Tx" -89.363639169999999;
	setAttr ".RightHandIndex4Ty" 146.78871169999999;
	setAttr ".RightHandIndex4Tz" 3.164250215;
	setAttr ".RightHandIndex4Ry" -2.0000646359999998;
	setAttr ".RightHandMiddle1Tx" -80.519627299999996;
	setAttr ".RightHandMiddle1Ty" 147.0898718;
	setAttr ".RightHandMiddle1Tz" 1.305458427;
	setAttr ".RightHandMiddle1Ry" -2.0000646579999999;
	setAttr ".RightHandMiddle2Tx" -85.379921789999997;
	setAttr ".RightHandMiddle2Ty" 147.08987139999999;
	setAttr ".RightHandMiddle2Tz" 1.1358596750000001;
	setAttr ".RightHandMiddle2Ry" -2.0000646359999998;
	setAttr ".RightHandMiddle3Tx" -88.143476890000002;
	setAttr ".RightHandMiddle3Ty" 147.0898712;
	setAttr ".RightHandMiddle3Tz" 1.039426113;
	setAttr ".RightHandMiddle3Ry" -2.0000646359999998;
	setAttr ".RightHandMiddle4Tx" -90.147889570000004;
	setAttr ".RightHandMiddle4Ty" 147.089871;
	setAttr ".RightHandMiddle4Tz" 0.96948263800000001;
	setAttr ".RightHandMiddle4Ry" -2.0000646359999998;
	setAttr ".RightHandRing1Tx" -80.603693699999994;
	setAttr ".RightHandRing1Ty" 146.968899;
	setAttr ".RightHandRing1Tz" -0.79237675600000002;
	setAttr ".RightHandRing1Ry" -2.0000646579999999;
	setAttr ".RightHandRing2Tx" -85.138693309999994;
	setAttr ".RightHandRing2Ty" 146.96889859999999;
	setAttr ".RightHandRing2Tz" -0.95062442800000002;
	setAttr ".RightHandRing2Ry" -2.0000646359999998;
	setAttr ".RightHandRing3Tx" -87.441817880000002;
	setAttr ".RightHandRing3Ty" 146.9688984;
	setAttr ".RightHandRing3Tz" -1.0309913799999999;
	setAttr ".RightHandRing3Ry" -2.0000646359999998;
	setAttr ".RightHandRing4Tx" -89.363995799999998;
	setAttr ".RightHandRing4Ty" 146.96889830000001;
	setAttr ".RightHandRing4Tz" -1.0980652959999999;
	setAttr ".RightHandRing4Ry" -2.0000646359999998;
	setAttr ".RightHandPinky1Tx" -80.592357370000002;
	setAttr ".RightHandPinky1Ty" 146.2759509;
	setAttr ".RightHandPinky1Tz" -2.4895741939999998;
	setAttr ".RightHandPinky1Ry" -2.0000646579999999;
	setAttr ".RightHandPinky1Rz" 0.0012412149999999999;
	setAttr ".RightHandPinky2Tx" -83.638299989999993;
	setAttr ".RightHandPinky2Ty" 146.27588489999999;
	setAttr ".RightHandPinky2Tz" -2.5958615950000001;
	setAttr ".RightHandPinky2Ry" -2.0000646359999998;
	setAttr ".RightHandPinky2Rz" 0.0012412149999999999;
	setAttr ".RightHandPinky3Tx" -85.613997130000001;
	setAttr ".RightHandPinky3Ty" 146.27584210000001;
	setAttr ".RightHandPinky3Tz" -2.6648030450000002;
	setAttr ".RightHandPinky3Ry" -2.0000646359999998;
	setAttr ".RightHandPinky3Rz" 0.0012412149999999999;
	setAttr ".RightHandPinky4Tx" -87.28162098;
	setAttr ".RightHandPinky4Ty" 146.27580589999999;
	setAttr ".RightHandPinky4Tz" -2.7229943639999998;
	setAttr ".RightHandPinky4Ry" -2.0000646359999998;
	setAttr ".RightHandPinky4Rz" 0.0012412149999999999;
	setAttr ".RightHandExtraFinger1Tx" -80.592357370000002;
	setAttr ".RightHandExtraFinger1Ty" 146.78871240000001;
	setAttr ".RightHandExtraFinger1Tz" -4.4895741940000002;
	setAttr ".RightHandExtraFinger1Ry" -2.0000646579999999;
	setAttr ".RightHandExtraFinger2Tx" -82.638299989999993;
	setAttr ".RightHandExtraFinger2Ty" 146.7887121;
	setAttr ".RightHandExtraFinger2Tz" -4.5958615949999997;
	setAttr ".RightHandExtraFinger2Ry" -2.0000646359999998;
	setAttr ".RightHandExtraFinger3Tx" -84.613997130000001;
	setAttr ".RightHandExtraFinger3Ty" 146.78871179999999;
	setAttr ".RightHandExtraFinger3Tz" -4.6648030450000002;
	setAttr ".RightHandExtraFinger3Ry" -2.0000646359999998;
	setAttr ".RightHandExtraFinger4Tx" -86.28162098;
	setAttr ".RightHandExtraFinger4Ty" 146.78871169999999;
	setAttr ".RightHandExtraFinger4Tz" -4.7229943639999998;
	setAttr ".RightHandExtraFinger4Ry" -2.0000646359999998;
	setAttr ".LeftFootThumb1Tx" 6.18422217;
	setAttr ".LeftFootThumb1Ty" 4.9992492679999998;
	setAttr ".LeftFootThumb1Tz" 1.930123209;
	setAttr ".LeftFootThumb2Tx" 4.551409713;
	setAttr ".LeftFootThumb2Ty" 2.6643834059999998;
	setAttr ".LeftFootThumb2Tz" 3.591937658;
	setAttr ".LeftFootThumb3Tx" 3.4619466889999999;
	setAttr ".LeftFootThumb3Ty" 1.8880788850000001;
	setAttr ".LeftFootThumb3Tz" 6.4001420700000002;
	setAttr ".LeftFootThumb4Tx" 3.4619466999999999;
	setAttr ".LeftFootThumb4Ty" 1.8880788550000001;
	setAttr ".LeftFootThumb4Tz" 9.6971958839999992;
	setAttr ".LeftFootIndex1Tx" 7.1105199680000002;
	setAttr ".LeftFootIndex1Ty" 1.888079117;
	setAttr ".LeftFootIndex1Tz" 12.9547209;
	setAttr ".LeftFootIndex2Tx" 7.1105199749999999;
	setAttr ".LeftFootIndex2Ty" 1.8880790999999999;
	setAttr ".LeftFootIndex2Tz" 14.82972745;
	setAttr ".LeftFootIndex3Tx" 7.1105199810000004;
	setAttr ".LeftFootIndex3Ty" 1.888079083;
	setAttr ".LeftFootIndex3Tz" 16.76314442;
	setAttr ".LeftFootIndex4Tx" 7.1105199880000001;
	setAttr ".LeftFootIndex4Ty" 1.8880790649999999;
	setAttr ".LeftFootIndex4Tz" 18.850666449999999;
	setAttr ".LeftFootMiddle1Tx" 8.9167242489999996;
	setAttr ".LeftFootMiddle1Ty" 1.888079163;
	setAttr ".LeftFootMiddle1Tz" 12.9547209;
	setAttr ".LeftFootMiddle2Tx" 8.9167242550000001;
	setAttr ".LeftFootMiddle2Ty" 1.888079147;
	setAttr ".LeftFootMiddle2Tz" 14.82860045;
	setAttr ".LeftFootMiddle3Tx" 8.9167242610000006;
	setAttr ".LeftFootMiddle3Ty" 1.888079131;
	setAttr ".LeftFootMiddle3Tz" 16.64971237;
	setAttr ".LeftFootMiddle4Tx" 8.9167242669999993;
	setAttr ".LeftFootMiddle4Ty" 1.8880791139999999;
	setAttr ".LeftFootMiddle4Tz" 18.565581959999999;
	setAttr ".LeftFootRing1Tx" 10.723903740000001;
	setAttr ".LeftFootRing1Ty" 1.888079211;
	setAttr ".LeftFootRing1Tz" 12.9547209;
	setAttr ".LeftFootRing2Tx" 10.723903740000001;
	setAttr ".LeftFootRing2Ty" 1.888079195;
	setAttr ".LeftFootRing2Tz" 14.71345226;
	setAttr ".LeftFootRing3Tx" 10.72390375;
	setAttr ".LeftFootRing3Ty" 1.8880791800000001;
	setAttr ".LeftFootRing3Tz" 16.472174209999999;
	setAttr ".LeftFootRing4Tx" 10.723903760000001;
	setAttr ".LeftFootRing4Ty" 1.8880791640000001;
	setAttr ".LeftFootRing4Tz" 18.27484922;
	setAttr ".LeftFootPinky1Tx" 12.52979668;
	setAttr ".LeftFootPinky1Ty" 1.888079257;
	setAttr ".LeftFootPinky1Tz" 12.9547209;
	setAttr ".LeftFootPinky2Tx" 12.52979669;
	setAttr ".LeftFootPinky2Ty" 1.8880792420000001;
	setAttr ".LeftFootPinky2Tz" 14.5796458;
	setAttr ".LeftFootPinky3Tx" 12.52979669;
	setAttr ".LeftFootPinky3Ty" 1.8880792289999999;
	setAttr ".LeftFootPinky3Tz" 16.143599309999999;
	setAttr ".LeftFootPinky4Tx" 12.5297967;
	setAttr ".LeftFootPinky4Ty" 1.8880792129999999;
	setAttr ".LeftFootPinky4Tz" 17.861196199999998;
	setAttr ".LeftFootExtraFinger1Tx" 5.0860939849999998;
	setAttr ".LeftFootExtraFinger1Ty" 1.888079254;
	setAttr ".LeftFootExtraFinger1Tz" 12.9547209;
	setAttr ".LeftFootExtraFinger2Tx" 5.0860939910000003;
	setAttr ".LeftFootExtraFinger2Ty" 1.888079236;
	setAttr ".LeftFootExtraFinger2Tz" 14.94401483;
	setAttr ".LeftFootExtraFinger3Tx" 5.0860939979999999;
	setAttr ".LeftFootExtraFinger3Ty" 1.8880792179999999;
	setAttr ".LeftFootExtraFinger3Tz" 16.99182682;
	setAttr ".LeftFootExtraFinger4Tx" 5.0860940049999996;
	setAttr ".LeftFootExtraFinger4Ty" 1.8880791990000001;
	setAttr ".LeftFootExtraFinger4Tz" 19.0793827;
	setAttr ".RightFootThumb1Tx" -6.180000014;
	setAttr ".RightFootThumb1Ty" 4.9992496019999999;
	setAttr ".RightFootThumb1Tz" 1.930123112;
	setAttr ".RightFootThumb2Tx" -4.5499999820000001;
	setAttr ".RightFootThumb2Ty" 2.6643838419999999;
	setAttr ".RightFootThumb2Tz" 3.5919375690000002;
	setAttr ".RightFootThumb3Tx" -3.4599999860000001;
	setAttr ".RightFootThumb3Ty" 1.888079335;
	setAttr ".RightFootThumb3Tz" 6.4001419850000003;
	setAttr ".RightFootThumb4Tx" -3.4599999860000001;
	setAttr ".RightFootThumb4Ty" 1.8880793090000001;
	setAttr ".RightFootThumb4Tz" 9.6971957989999993;
	setAttr ".RightFootIndex1Tx" -7.1099999839999999;
	setAttr ".RightFootIndex1Ty" 1.888079262;
	setAttr ".RightFootIndex1Tz" 12.95472064;
	setAttr ".RightFootIndex2Tx" -7.1099999839999999;
	setAttr ".RightFootIndex2Ty" 1.8880792479999999;
	setAttr ".RightFootIndex2Tz" 14.82972719;
	setAttr ".RightFootIndex3Tx" -7.1099999839999999;
	setAttr ".RightFootIndex3Ty" 1.8880792340000001;
	setAttr ".RightFootIndex3Tz" 16.76314416;
	setAttr ".RightFootIndex4Tx" -7.1099999839999999;
	setAttr ".RightFootIndex4Ty" 1.8880792179999999;
	setAttr ".RightFootIndex4Tz" 18.850666189999998;
	setAttr ".RightFootMiddle1Tx" -8.92;
	setAttr ".RightFootMiddle1Ty" 1.8880792049999999;
	setAttr ".RightFootMiddle1Tz" 12.954720630000001;
	setAttr ".RightFootMiddle2Tx" -8.92;
	setAttr ".RightFootMiddle2Ty" 1.8880791910000001;
	setAttr ".RightFootMiddle2Tz" 14.82860018;
	setAttr ".RightFootMiddle3Tx" -8.92;
	setAttr ".RightFootMiddle3Ty" 1.8880791770000001;
	setAttr ".RightFootMiddle3Tz" 16.649712099999999;
	setAttr ".RightFootMiddle4Tx" -8.92;
	setAttr ".RightFootMiddle4Ty" 1.8880791619999999;
	setAttr ".RightFootMiddle4Tz" 18.565581689999998;
	setAttr ".RightFootRing1Tx" -10.72;
	setAttr ".RightFootRing1Ty" 1.8880791610000001;
	setAttr ".RightFootRing1Tz" 12.95472062;
	setAttr ".RightFootRing2Tx" -10.72;
	setAttr ".RightFootRing2Ty" 1.888079147;
	setAttr ".RightFootRing2Tz" 14.713451989999999;
	setAttr ".RightFootRing3Tx" -10.72;
	setAttr ".RightFootRing3Ty" 1.888079134;
	setAttr ".RightFootRing3Tz" 16.472173940000001;
	setAttr ".RightFootRing4Tx" -10.72;
	setAttr ".RightFootRing4Ty" 1.88807912;
	setAttr ".RightFootRing4Tz" 18.274848949999999;
	setAttr ".RightFootPinky1Tx" -12.530000060000001;
	setAttr ".RightFootPinky1Ty" 1.8880791029999999;
	setAttr ".RightFootPinky1Tz" 12.95472062;
	setAttr ".RightFootPinky2Tx" -12.530000060000001;
	setAttr ".RightFootPinky2Ty" 1.888079091;
	setAttr ".RightFootPinky2Tz" 14.57964552;
	setAttr ".RightFootPinky3Tx" -12.530000060000001;
	setAttr ".RightFootPinky3Ty" 1.8880790789999999;
	setAttr ".RightFootPinky3Tz" 16.143599040000002;
	setAttr ".RightFootPinky4Tx" -12.530000060000001;
	setAttr ".RightFootPinky4Ty" 1.888079066;
	setAttr ".RightFootPinky4Tz" 17.86119592;
	setAttr ".RightFootExtraFinger1Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger1Ty" 1.8880791260000001;
	setAttr ".RightFootExtraFinger1Tz" 12.95472064;
	setAttr ".RightFootExtraFinger2Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger2Ty" 1.8880791109999999;
	setAttr ".RightFootExtraFinger2Tz" 14.944014579999999;
	setAttr ".RightFootExtraFinger3Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger3Ty" 1.888079096;
	setAttr ".RightFootExtraFinger3Tz" 16.99182656;
	setAttr ".RightFootExtraFinger4Tx" -5.0900000030000001;
	setAttr ".RightFootExtraFinger4Ty" 1.88807908;
	setAttr ".RightFootExtraFinger4Tz" 19.079382450000001;
	setAttr ".LeftInHandThumbTx" 71.709864199999998;
	setAttr ".LeftInHandThumbTy" 146.58868419999999;
	setAttr ".LeftInHandIndexTx" 71.709864199999998;
	setAttr ".LeftInHandIndexTy" 146.58868419999999;
	setAttr ".LeftInHandMiddleTx" 71.709864199999998;
	setAttr ".LeftInHandMiddleTy" 146.58868419999999;
	setAttr ".LeftInHandRingTx" 71.709864199999998;
	setAttr ".LeftInHandRingTy" 146.58868419999999;
	setAttr ".LeftInHandPinkyTx" 71.709864199999998;
	setAttr ".LeftInHandPinkyTy" 146.58868419999999;
	setAttr ".LeftInHandExtraFingerTx" 71.709864199999998;
	setAttr ".LeftInHandExtraFingerTy" 146.58868419999999;
	setAttr ".RightInHandThumbTx" -71.709861489999994;
	setAttr ".RightInHandThumbTy" 146.58897870000001;
	setAttr ".RightInHandIndexTx" -71.709861489999994;
	setAttr ".RightInHandIndexTy" 146.58897870000001;
	setAttr ".RightInHandMiddleTx" -71.709861489999994;
	setAttr ".RightInHandMiddleTy" 146.58897870000001;
	setAttr ".RightInHandRingTx" -71.709861489999994;
	setAttr ".RightInHandRingTy" 146.58897870000001;
	setAttr ".RightInHandPinkyTx" -71.709861489999994;
	setAttr ".RightInHandPinkyTy" 146.58897870000001;
	setAttr ".RightInHandExtraFingerTx" -71.709861489999994;
	setAttr ".RightInHandExtraFingerTy" 146.58897870000001;
	setAttr ".LeftInFootThumbTx" 8.9100008010000007;
	setAttr ".LeftInFootThumbTy" 8.15039625;
	setAttr ".LeftInFootIndexTx" 8.9100008010000007;
	setAttr ".LeftInFootIndexTy" 8.1503963469999992;
	setAttr ".LeftInFootMiddleTx" 8.9100008010000007;
	setAttr ".LeftInFootMiddleTy" 8.1503963469999992;
	setAttr ".LeftInFootRingTx" 8.9100008010000007;
	setAttr ".LeftInFootRingTy" 8.1503963469999992;
	setAttr ".LeftInFootPinkyTx" 8.9100008010000007;
	setAttr ".LeftInFootPinkyTy" 8.1503963469999992;
	setAttr ".LeftInFootExtraFingerTx" 8.9100008010000007;
	setAttr ".LeftInFootExtraFingerTy" 8.1503963469999992;
	setAttr ".RightInFootThumbTx" -8.9100025980000002;
	setAttr ".RightInFootThumbTy" 8.1503963929999994;
	setAttr ".RightInFootThumbTz" 0.00043882099999999999;
	setAttr ".RightInFootIndexTx" -8.9100026190000001;
	setAttr ".RightInFootIndexTy" 8.1503963939999995;
	setAttr ".RightInFootIndexTz" 0.00043882099999999999;
	setAttr ".RightInFootMiddleTx" -8.9100026190000001;
	setAttr ".RightInFootMiddleTy" 8.1503963939999995;
	setAttr ".RightInFootMiddleTz" 0.00043882099999999999;
	setAttr ".RightInFootRingTx" -8.9100026190000001;
	setAttr ".RightInFootRingTy" 8.1503963939999995;
	setAttr ".RightInFootRingTz" 0.00043882099999999999;
	setAttr ".RightInFootPinkyTx" -8.9100026190000001;
	setAttr ".RightInFootPinkyTy" 8.1503963939999995;
	setAttr ".RightInFootPinkyTz" 0.00043882099999999999;
	setAttr ".RightInFootExtraFingerTx" -8.9100026190000001;
	setAttr ".RightInFootExtraFingerTy" 8.1503963939999995;
	setAttr ".RightInFootExtraFingerTz" 0.00043882099999999999;
	setAttr ".LeftShoulderExtraTx" 12.353625535000001;
	setAttr ".LeftShoulderExtraTy" 146.58868419999999;
	setAttr ".RightShoulderExtraTx" -12.353637216499999;
	setAttr ".RightShoulderExtraTy" 146.58898;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "AE7B9E1F-4083-70D1-7B6D-95B85952AB07";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 945\n            -height 539\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n"
		+ "            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n"
		+ "            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n"
		+ "                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 5\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n"
		+ "                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n"
		+ "                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n"
		+ "                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n"
		+ "                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n"
		+ "                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n"
		+ "                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n"
		+ "\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n"
		+ "                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n"
		+ "                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 945\\n    -height 539\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 945\\n    -height 539\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "D64CDA6C-4C97-A1B5-E649-EAA74CE965E9";
	setAttr ".b" -type "string" "playbackOptions -min 6 -max 421 -ast 6 -aet 1000 ";
	setAttr ".st" 6;
createNode animCurveTL -n "Character1_RightHandPinky4_translateX";
	rename -uid "19D4A5CA-4327-9BFD-4E43-0E8EFFFFDD50";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.12957751750946045 170 -0.43977275490760803
		 180 0.26414394378662109 190 0.69707706570625305 200 0.773649662733078 210 0.74918568134307861
		 220 0.74236616492271423 230 0.72753354907035828 240 0.60941800475120544 250 0.02862587571144104
		 260 -0.61903148889541626 270 0.055318325757980347;
createNode animCurveTL -n "Character1_RightHandPinky4_translateY";
	rename -uid "C4BC075B-49B2-9B41-9FEF-CF9160BB7306";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.27639269828796387 170 0.33625960350036621
		 180 -1.0086089372634888 190 -0.7757239043712616 200 -0.85545703768730164 210 -0.81298425793647766
		 220 -0.70382729172706604 230 -0.72319507598876953 240 -0.72583705186843872 250 -0.90995728969573975
		 260 -0.060085952281951904 270 0.23498386144638062;
createNode animCurveTL -n "Character1_RightHandPinky4_translateZ";
	rename -uid "79CE8D80-4731-6A92-F0B9-F2BA49C4F414";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.25057699531316757 170 -0.21158242598176003
		 180 -0.17036888748407364 190 -0.11658612638711929 200 -0.16496060416102409 210 -0.11049974709749222
		 220 -0.076510850340127945 230 -0.028608553111553192 240 -0.09080786257982254 250 -0.033288728445768356
		 260 -0.1471029594540596 270 -0.47368467785418034;
createNode animCurveTL -n "Character1_RightHandPinky3_translateX";
	rename -uid "69DC1D51-4665-D036-8914-77A94BDE973F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.30592158436775208 170 -0.027740746736526489
		 180 1.0801680386066437 190 1.0742917656898499 200 1.0831542313098907 210 1.0627783834934235
		 220 1.036515086889267 230 1.0277643799781799 240 0.989580899477005 250 0.76749399304389954
		 260 -0.2258889377117157 270 0.70801600813865662;
createNode animCurveTL -n "Character1_RightHandPinky3_translateY";
	rename -uid "1A0C1FC5-4184-C520-B48F-6EA2FEA5FF98";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.66874176263809204 170 -0.18473267555236816
		 180 -0.64967572689056396 190 -0.081389397382736206 200 -0.036379694938659668 210 -0.025038421154022217
		 220 0.021012872457504272 230 -0.02180635929107666 240 -0.067240744829177856 250 -0.85686296224594116
		 260 -0.86752921342849731 270 -0.48534572124481201;
createNode animCurveTL -n "Character1_RightHandPinky3_translateZ";
	rename -uid "5A548757-4F94-5C93-1D06-6EBA37589E1F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.60332883149385452 170 -0.73716575279831886
		 180 -0.0076255761086940765 190 -0.13263523578643799 200 -0.11305287480354309 210 -0.04948033019900322
		 220 -0.021251197904348373 230 0.0085950829088687897 240 -0.12650750577449799 250 -0.089437421411275864
		 260 -0.77302940189838409 270 -0.82565182819962502;
createNode animCurveTL -n "Character1_RightHandPinky2_translateX";
	rename -uid "22F35B74-4699-8CC3-A3C6-7F86281C3B9D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.348433643579483 170 1.7265379428863525
		 180 1.5791080892086029 190 1.4394834637641907 200 1.4242596924304962 210 1.3975180685520172
		 220 1.3930007815361023 230 1.3460800051689148 240 1.3685613870620728 250 1.4477111399173737
		 260 1.1468388140201569 270 1.4082737267017365;
createNode animCurveTL -n "Character1_RightHandPinky2_translateY";
	rename -uid "08F37190-454D-7042-DDBC-4882F11C1129";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 2.2600293159484863 170 -1.0929599404335022
		 180 2.1644152700901031 190 2.2194921970367432 200 2.4805381894111633 210 2.3695684969425201
		 220 2.2506147623062134 230 2.2767551243305206 240 2.2618576884269714 250 1.3639725744724274
		 260 -2.6724323630332947 270 -1.9738823175430298;
createNode animCurveTL -n "Character1_RightHandPinky2_translateZ";
	rename -uid "DB780E28-44B5-F277-5B51-99A04540C253";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.95488037914037704 170 -0.30240649357438087
		 180 0.59401961043477058 190 0.29556434601545334 200 0.45453272759914398 210 0.5015951581299305
		 220 0.48296162858605385 230 0.44727707281708717 240 0.27963761240243912 250 0.72319312021136284
		 260 -0.080280192196369171 270 -0.27897991240024567;
createNode animCurveTL -n "Character1_RightHandPinky1_translateX";
	rename -uid "2A068189-4CA9-C25E-739E-C1906671DCC5";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -1.0986216366291046 170 1.1804066598415375
		 180 0.20613446831703186 190 -0.44517070055007935 200 -0.27790367603302002 210 -0.29855892062187195
		 220 -0.34975782036781311 230 -0.49882829189300537 240 -0.41563957929611206 250 -0.62514916062355042
		 260 0.60940906405448914 270 -1.3677231967449188;
createNode animCurveTL -n "Character1_RightHandPinky1_translateY";
	rename -uid "BBD85AC3-4A2E-21C2-FCC3-E39803808959";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.23284256458282471 170 0.077444314956665039
		 180 5.3135611116886139 190 5.5865451693534851 200 5.0771020352840424 210 4.9166478216648102
		 220 4.9641162157058716 230 4.8596687614917755 240 4.6598263084888458 250 4.4106200337409973
		 260 -2.1357893943786621 270 -4.12445068359375;
createNode animCurveTL -n "Character1_RightHandPinky1_translateZ";
	rename -uid "707A83B3-43D0-A3CD-A0B7-14A664ABB73B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 4.9407083654386952 170 4.5326761524847825
		 180 3.2932578324107453 190 2.6601975940593547 200 2.6217725847345719 210 2.479485577896412
		 220 2.3408234224916669 230 2.3325964451032632 240 2.3427989241099567 250 3.9166059905255679
		 260 5.973350733938787 270 2.8536413403116967;
createNode animCurveTL -n "Character1_RightHandRing4_translateX";
	rename -uid "FC6C9019-4513-B93C-8A41-B2A4CF9B8BA9";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.28680190443992615 170 -0.42617172002792358
		 180 0.038583576679229736 190 0.67715942859649658 200 0.80813392996788025 210 0.76395124197006226
		 220 0.78025907278060913 230 0.79387128353118896 240 0.5955912172794342 250 -0.086541473865509033
		 260 -0.57279467582702637 270 -0.070041418075561523;
createNode animCurveTL -n "Character1_RightHandRing4_translateY";
	rename -uid "DF967A99-4AA3-4C9D-8B7D-F3B8BB19237F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.013370811939239502 170 0.20527392625808716
		 180 -1.4944396913051605 190 -1.299528032541275 200 -1.1216148734092712 210 -1.1584371328353882
		 220 -1.0231509804725647 230 -1.0151579976081848 240 -1.0605521500110626 250 -1.1148355901241302
		 260 -0.03996044397354126 270 0.23323595523834229;
createNode animCurveTL -n "Character1_RightHandRing4_translateZ";
	rename -uid "11105BDD-4CDF-B42A-7DE6-DEBCE0225B37";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.76474277302622795 170 -0.23235194385051727
		 180 -0.379962008446455 190 -0.085289916023612022 200 -0.18690596334636211 210 -0.15664785169064999
		 220 -0.13858596794307232 230 -0.10336786508560181 240 -0.15380373224616051 250 -0.40747588500380516
		 260 -0.21306853741407394 270 -0.78818458132445812;
createNode animCurveTL -n "Character1_RightHandRing3_translateX";
	rename -uid "4FEBBC9E-4B48-B28E-7B4D-7FA88DB198F7";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.23775771260261536 170 -0.0035583972930908203
		 180 1.1097684502601624 190 1.369176059961319 200 1.4868602156639099 210 1.4295570552349091
		 220 1.4102384448051453 230 1.4225251972675323 240 1.3145104050636292 250 0.80044940114021301
		 260 -0.16715303063392639 270 0.74252709746360779;
createNode animCurveTL -n "Character1_RightHandRing3_translateY";
	rename -uid "0540A63F-4F26-BAA1-6112-33835A24ED0C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.52295923233032227 170 -0.56619197130203247
		 180 -1.507200300693512 190 -0.76279565691947937 200 -0.45283064246177673 210 -0.49070790410041809
		 220 -0.39487257599830627 230 -0.40104612708091736 240 -0.54126977920532227 250 -1.533074676990509
		 260 -1.1262863874435425 270 -0.61527639627456665;
createNode animCurveTL -n "Character1_RightHandRing3_translateZ";
	rename -uid "B75C89D2-44A0-C664-AC55-168ED9B80F41";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -1.6205881722271442 170 -0.88031552731990814
		 180 -0.097192078828811646 190 0.032386835664510727 200 -0.084432866424322128 210 -0.025081029161810875
		 220 0.0215163454413414 230 0.077433139085769653 240 -0.060673942789435387 250 -0.43113632127642632
		 260 -0.99404677748680115 270 -1.5931650996208191;
createNode animCurveTL -n "Character1_RightHandRing2_translateX";
	rename -uid "663CCEB9-4019-6093-669C-989D7BA28D65";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.4095880091190338 170 2.0799838006496429
		 180 1.8289178609848022 190 1.6608841717243195 200 1.6997940838336945 210 1.6277991235256195
		 220 1.6193658113479614 230 1.6032949090003967 240 1.6396120190620422 250 1.8070243299007416
		 260 1.3558007776737213 270 1.5454508364200592;
createNode animCurveTL -n "Character1_RightHandRing2_translateY";
	rename -uid "2E43DCA7-4875-8B37-2A38-05A6DFD677B3";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 3.4636527299880981 170 -1.7799854278564453
		 180 2.2947929799556732 190 2.5232747197151184 200 2.8031341731548309 210 2.6619270443916321
		 220 2.4634480476379395 230 2.4750418961048126 240 2.5236189365386963 250 1.6129732131958008
		 260 -3.4136205911636353 270 -2.761329710483551;
createNode animCurveTL -n "Character1_RightHandRing2_translateZ";
	rename -uid "E1DCC7AD-4FCA-4D74-CF96-1DAF694F0A92";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.77178720384836197 170 0.052115879952907562
		 180 1.1753773782402277 190 0.70497184060513973 200 0.72662383317947388 210 0.72553600184619427
		 220 0.75749368406832218 230 0.7775651291012764 240 0.63339457847177982 250 1.4167453162372112
		 260 0.32349564135074615 270 -0.05339551717042923;
createNode animCurveTL -n "Character1_RightHandRing1_translateX";
	rename -uid "0AC97D52-4692-40C8-BDFD-9E80A7E9C8E6";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.62739774584770203 170 0.85767880082130432
		 180 0.36408528685569763 190 -0.55544301867485046 200 -0.63150376081466675 210 -0.53997337818145752
		 220 -0.56962966918945312 230 -0.68462714552879333 240 -0.6876334547996521 250 -0.47922581434249878
		 260 0.70612728595733643 270 -0.94316974282264709;
createNode animCurveTL -n "Character1_RightHandRing1_translateY";
	rename -uid "011569E1-4F11-9940-3B2C-F58ECEBB8687";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.21113455295562744 170 1.7862170934677124
		 180 6.7203372716903687 190 6.6553473472595215 200 6.0326278209686279 210 5.8544263243675232
		 220 5.854768306016922 230 5.7084359228610992 240 5.5556461215019226 250 5.8782599866390228
		 260 0.19597560167312622 270 -3.0723005533218384;
createNode animCurveTL -n "Character1_RightHandRing1_translateZ";
	rename -uid "775BA609-4F6D-3F38-17F8-3798F98F23F5";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 5.4829375931603863 170 4.825556613104709
		 180 2.1628577465889975 190 1.4185776159592933 200 1.5331755646002421 210 1.4268140932472306
		 220 1.3548820850701304 230 1.3356058035242313 240 1.3919168524807901 250 3.1708669477666263
		 260 6.0698258806496597 270 3.8784466290735509;
createNode animCurveTL -n "Character1_RightHandMiddle4_translateX";
	rename -uid "ADF822F3-4306-EED5-50DE-07A2D33CE137";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.43922290205955505 170 -0.38384869694709778
		 180 -0.12441202998161316 190 0.56309401988983154 200 0.67232474684715271 210 0.63840374350547791
		 220 0.66926032304763794 230 0.69573819637298584 240 0.50261914730072021 250 -0.12812018394470215
		 260 -0.57077854871749878 270 -0.092741847038269043;
createNode animCurveTL -n "Character1_RightHandMiddle4_translateY";
	rename -uid "866B867C-45B4-1783-6B84-31BAB5934CA6";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.41764676570892334 170 -0.13289898633956909
		 180 -1.5309266746044159 190 -1.253141462802887 200 -1.133398711681366 210 -1.1610008776187897
		 220 -1.0462045669555664 230 -1.0259203612804413 240 -1.1257097125053406 250 -1.196993887424469
		 260 -0.78443437814712524 270 0.021515786647796631;
createNode animCurveTL -n "Character1_RightHandMiddle4_translateZ";
	rename -uid "D165B7B5-48B7-1A49-DB78-6CBB233B8C98";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.084700249135494232 170 -0.12289714068174362
		 180 -0.23197336122393608 190 -0.10510571300983429 200 -0.31554652377963066 210 -0.25642421096563339
		 220 -0.26877347845584154 230 -0.21624402143061161 240 -0.3512864001095295 250 -0.44457558542490005
		 260 -0.013551861047744751 270 -0.89948466047644615;
createNode animCurveTL -n "Character1_RightHandMiddle3_translateX";
	rename -uid "456C4FE2-4452-DB86-1395-3F8EC78D44F0";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.2099454402923584 170 0.15588328242301941
		 180 0.97810998558998108 190 1.3535454869270325 200 1.4671280980110168 210 1.4149032533168793
		 220 1.400236040353775 230 1.4102563261985779 240 1.2944318354129791 250 0.75376331806182861
		 260 0.0239543616771698 270 0.75471550226211548;
createNode animCurveTL -n "Character1_RightHandMiddle3_translateY";
	rename -uid "45112894-42A1-DC14-85F3-E08687A5B978";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.7260248064994812 170 -0.85749328136444092
		 180 -1.7231181263923645 190 -0.88935121893882751 200 -0.57447329163551331 210 -0.5878061056137085
		 220 -0.51497966051101685 230 -0.48029422760009766 240 -0.77867880463600159 250 -1.8927343189716339
		 260 -1.626451313495636 270 -0.8307337760925293;
createNode animCurveTL -n "Character1_RightHandMiddle3_translateZ";
	rename -uid "29E13D4D-4E18-10A3-A530-5699458E96FB";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.90905316174030304 170 -0.84984339773654938
		 180 0.2065212931483984 190 0.25796955451369286 200 -0.03845652099698782 210 0.042622396722435951
		 220 0.071894237771630287 230 0.19459545146673918 240 -0.045824004337191582 250 -0.20251013338565826
		 260 -0.82034189254045486 270 -1.3980209827423096;
createNode animCurveTL -n "Character1_RightHandMiddle2_translateX";
	rename -uid "C7E95EAC-49F0-2B0A-2A59-35945C82C335";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.3910762965679169 170 2.2110655903816223
		 180 1.7471864819526672 190 1.6569793224334717 200 1.7971649765968323 210 1.6556829214096069
		 220 1.6227163374423981 230 1.5899933874607086 240 1.6845881938934326 250 1.8452122807502747
		 260 1.3311780989170074 270 1.3456352055072784;
createNode animCurveTL -n "Character1_RightHandMiddle2_translateY";
	rename -uid "BC5ED5CE-4ED2-42CD-DEBF-8989B8C386E7";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 3.6373928189277649 170 -2.0350411534309387
		 180 2.2618353366851807 190 2.4363778531551361 200 2.7164295315742493 210 2.5944449007511139
		 220 2.4157583713531494 230 2.389845997095108 240 2.4285323917865753 250 1.6435839235782623
		 260 -3.0258893966674805 270 -3.2132551074028015;
createNode animCurveTL -n "Character1_RightHandMiddle2_translateZ";
	rename -uid "42C70288-434E-08CA-CAF5-28A450ED329E";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.86204521358013153 170 0.73509626090526581
		 180 1.2799778720363975 190 0.81186129245907068 200 0.71258156094700098 210 0.71436620783060789
		 220 0.72987723397091031 230 0.80518175382167101 240 0.60785086825489998 250 1.6845007427036762
		 260 0.79260002821683884 270 0.14326181262731552;
createNode animCurveTL -n "Character1_RightHandMiddle1_translateX";
	rename -uid "D97A466A-4E96-FB53-2796-B88340587C06";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.024332106113433838 170 0.65669417381286621
		 180 0.83453580737113953 190 -0.23726150393486023 200 -0.50252750515937805 210 -0.33769458532333374
		 220 -0.38233324885368347 230 -0.47899112105369568 240 -0.51876381039619446 250 -0.03941953182220459
		 260 0.9043671190738678 270 -0.19261389970779419;
createNode animCurveTL -n "Character1_RightHandMiddle1_translateY";
	rename -uid "C4F232E4-4ED7-51E7-C260-38850E85DF4B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.1250346899032593 170 3.2649636268615723
		 180 7.5203843414783478 190 7.3372051119804382 200 6.7075811326503754 210 6.4820587635040283
		 220 6.4508914947509766 230 6.2774017453193665 240 6.1968214809894562 250 6.8190045654773712
		 260 2.2379949688911438 270 -1.7812594771385193;
createNode animCurveTL -n "Character1_RightHandMiddle1_translateZ";
	rename -uid "7A3E5291-4375-7980-2212-9C946DFEF414";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 6.205744866429086 170 5.1834012936524232
		 180 0.93409078835975379 190 0.12276199818188616 200 0.36453688726396649 210 0.31043371836858569
		 220 0.30837098493066151 230 0.29514996485886513 240 0.40592508394183824 250 2.4548442663217429
		 260 6.1636272002488113 270 4.9861455874406602;
createNode animCurveTL -n "Character1_RightHandIndex4_translateX";
	rename -uid "FD18EAA8-4D84-38DF-7B15-FFAB9CFD7F09";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.40170773863792419 170 -0.29553696513175964
		 180 0.049795210361480713 190 0.65211653709411621 200 0.65829455852508545 210 0.63858926296234131
		 220 0.64913257956504822 230 0.70174857974052429 240 0.52854269742965698 250 -0.095061957836151123
		 260 -0.3276139497756958 270 -0.011073052883148193;
createNode animCurveTL -n "Character1_RightHandIndex4_translateY";
	rename -uid "13AB428D-4EF5-FAA5-E4D8-C68FF5712E6C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.62474459409713745 170 -0.24964213371276855
		 180 -1.5715979039669037 190 -1.1813655495643616 200 -1.0082133114337921 210 -1.0486766695976257
		 220 -0.90624019503593445 230 -0.8973442018032074 240 -0.97280368208885193 250 -1.2688368558883667
		 260 -0.95674842596054077 270 -0.074395537376403809;
createNode animCurveTL -n "Character1_RightHandIndex4_translateZ";
	rename -uid "0ABB3DE5-4D9E-9381-7830-2597BA55FD85";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.27111824601888657 170 0.17027221620082855
		 180 -0.002729916013777256 190 0.17688366933725774 200 -0.13537220656871796 210 -0.053542715613730252
		 220 -0.11559266567928717 230 -0.039124960312619805 240 -0.20702961628558114 250 -0.58498391881585121
		 260 0.28557479381561279 270 -0.72028711438179016;
createNode animCurveTL -n "Character1_RightHandIndex3_translateX";
	rename -uid "68E931A9-4DD3-8A43-A9AC-43A8C0DB88F2";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.074093788862228394 170 0.13155117630958557
		 180 0.90662464499473572 190 1.24659463763237 200 1.249781996011734 210 1.2169204652309418
		 220 1.1942446231842041 230 1.2206554412841797 240 1.1364385485649109 250 0.62437355518341064
		 260 0.10692402720451355 270 0.41832402348518372;
createNode animCurveTL -n "Character1_RightHandIndex3_translateY";
	rename -uid "580CFFA1-4A2D-F65A-5A69-94B3BC6468DC";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.4112800359725952 170 -1.1044777929782867
		 180 -1.7748378217220306 190 -0.54725110530853271 200 -0.37846416234970093 210 -0.3573194146156311
		 220 -0.2575412392616272 230 -0.219697505235672 240 -0.44678226113319397 250 -1.9015990197658539
		 260 -1.6982227563858032 270 -0.55688917636871338;
createNode animCurveTL -n "Character1_RightHandIndex3_translateZ";
	rename -uid "1087D95D-4773-5383-B15F-BDA943187F9B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.028535909950733185 170 0.20358189940452576
		 180 0.23494760971516371 190 0.49908821820281446 200 0.10720754507929087 210 0.1788719353498891
		 220 0.15166587982093915 230 0.27255939667156781 240 0.066810934367822483 250 -0.20097792148590088
		 260 0.24552438408136368 270 -0.78661032021045685;
createNode animCurveTL -n "Character1_RightHandIndex2_translateX";
	rename -uid "0814D618-463D-7814-FFC6-8DA8ECF9DDC5";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.87430179119110107 170 2.0521782338619232
		 180 1.3783827424049377 190 1.2020118534564972 200 1.4289423823356628 210 1.2714453041553497
		 220 1.2515366077423096 230 1.180393248796463 240 1.3486437499523163 250 1.6713961958885193
		 260 1.0449305176734924 270 0.8998967707157135;
createNode animCurveTL -n "Character1_RightHandIndex2_translateY";
	rename -uid "C9BC79E8-459A-9902-C84D-ABA9DEF76CB4";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 3.503689169883728 170 -1.6881220042705536
		 180 2.3252002894878387 190 2.2108376026153564 200 2.4687699973583221 210 2.4059414863586426
		 220 2.2958837449550629 230 2.2561870515346527 240 2.235858142375946 250 1.4376997947692871
		 260 -1.8519178032875061 270 -3.110562264919281;
createNode animCurveTL -n "Character1_RightHandIndex2_translateZ";
	rename -uid "C1FD55AE-4D5D-665E-2A37-92B0A69D1919";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.2404188513755798 170 0.97416657954454422
		 180 0.98508881055749953 190 0.73270364664494991 200 0.52139502950012684 210 0.53034800221212208
		 220 0.52299962262623012 230 0.61254127185748075 240 0.47614651921321638 250 1.423550583422184
		 260 1.2122137472033501 270 0.56168418377637863;
createNode animCurveTL -n "Character1_RightHandIndex1_translateX";
	rename -uid "BF61D95D-4EB3-DABF-701C-388B5E3CE137";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.9545937180519104 170 0.70317909121513367
		 180 1.4453977346420288 190 0.34713819622993469 200 -0.042188912630081177 210 0.15462487936019897
		 220 0.082341581583023071 230 0.0010952353477478027 240 -0.036723911762237549 250 0.6039641797542572
		 260 1.2206733226776123 270 1.0347984731197357;
createNode animCurveTL -n "Character1_RightHandIndex1_translateY";
	rename -uid "3624EFEC-467B-3292-745B-D99DE0C4E830";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 2.3331016302108765 170 4.339107871055603
		 180 7.7403992414474487 190 7.4908889830112457 200 6.8675927817821503 210 6.6158249974250793
		 220 6.5288655459880829 230 6.3804633915424347 240 6.3211888074874878 250 7.060309499502182
		 260 3.6182373762130737 270 -0.47943592071533203;
createNode animCurveTL -n "Character1_RightHandIndex1_translateZ";
	rename -uid "83DB0EF1-450C-BC04-A3FD-9FB72A1B976A";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 6.7805411407334759 170 5.3906891118458589
		 180 -0.24932858941610903 190 -1.0784637026063137 200 -0.73260841681985767 210 -0.72875840869528474
		 220 -0.63818871385592502 230 -0.61880570219727815 240 -0.49875810273078969 250 1.8225151674414519
		 260 6.0018408228188491 270 5.9081102328264024;
createNode animCurveTL -n "Character1_RightHandThumb4_translateX";
	rename -uid "2AF60D5D-4692-7EBF-EFCE-A291E96FC1B9";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.32551959156990051 170 0.80165639519691467
		 180 -0.18145591020584106 190 0.075750052928924561 200 0.0158652663230896 210 0.099427253007888794
		 220 -0.10957047343254089 230 -0.0069938600063323975 240 -0.087759643793106079 250 -0.39781630039215088
		 260 0.26473850011825562 270 0.016285479068756104;
createNode animCurveTL -n "Character1_RightHandThumb4_translateY";
	rename -uid "C4CAFB17-40D3-9920-5791-61AEF587D8B0";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -1.340465247631073 170 -1.2756630778312683
		 180 0.80649107694625854 190 1.3367749750614166 200 1.3101942837238312 210 1.2598380446434021
		 220 1.2786224484443665 230 1.3495065271854401 240 1.2280784547328949 250 0.39373934268951416
		 260 -1.1737078428268433 270 -2.0301550626754761;
createNode animCurveTL -n "Character1_RightHandThumb4_translateZ";
	rename -uid "B11B564C-46E5-4DB3-870E-5A8DCE272D65";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.95566101372241974 170 0.96893459558486938
		 180 1.1036205338314176 190 0.99060139618813992 200 1.0361297987401485 210 0.91032591881230474
		 220 0.83542296197265387 230 0.93306319322437048 240 0.93768483493477106 250 1.3108430430293083
		 260 1.6131224110722542 270 0.48272106796503067;
createNode animCurveTL -n "Character1_RightHandThumb3_translateX";
	rename -uid "93C65C31-4671-C995-91C5-D89181521DF1";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 0.61042830348014832 170 1.0165281593799591
		 180 0.81780776381492615 190 1.0147780179977417 200 0.98924338817596436 210 0.94541609287261963
		 220 0.9160749614238739 230 0.9188331663608551 240 0.93475654721260071 250 0.76107457280158997
		 260 0.79894959926605225 270 0.46346113085746765;
createNode animCurveTL -n "Character1_RightHandThumb3_translateY";
	rename -uid "7816A65E-4C3B-A4A3-E489-FA9BC91969E3";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -0.46338289976119995 170 -0.9027332067489624
		 180 1.4844506978988647 190 1.4766119420528412 200 1.5563473105430603 210 1.4497384428977966
		 220 1.5970610082149506 230 1.5149451792240143 240 1.6254700720310211 250 1.4066442847251892
		 260 -1.1762335896492004 270 -1.9099965691566467;
createNode animCurveTL -n "Character1_RightHandThumb3_translateZ";
	rename -uid "2B0BB7C3-44C4-B872-178C-2387FFBB7F6B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.086606178432703 170 1.0113414376974106
		 180 1.1272747186012566 190 0.93711081426590681 200 0.93322307802736759 210 0.78738830052316189
		 220 0.80222095130011439 230 0.87223404552787542 240 0.88600937160663307 250 1.5840785577893257
		 260 1.2639756314456463 270 0.53551755845546722;
createNode animCurveTL -n "Character1_RightHandThumb2_translateX";
	rename -uid "CC5228AE-4742-E140-7952-D58E17E298F7";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.1690787971019745 170 0.85613876581192017
		 180 1.1102244257926941 190 0.97913593053817749 200 0.98027586936950684 210 0.9745672345161438
		 220 1.0102361440658569 230 0.98410695791244507 240 1.0369308292865753 250 1.2081116437911987
		 260 0.99782869219779968 270 1.2695208191871643;
createNode animCurveTL -n "Character1_RightHandThumb2_translateY";
	rename -uid "E3B1DE19-4E8C-0EB3-D109-C29FC44D6ECF";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.2461364269256592 170 0.88561177253723145
		 180 2.190747857093811 190 2.0115628838539124 200 2.0180314779281616 210 2.0039454102516174
		 220 2.0268291234970093 230 1.9645415246486664 240 1.998920738697052 250 1.9353903830051422
		 260 0.37062764167785645 270 -0.63768625259399414;
createNode animCurveTL -n "Character1_RightHandThumb2_translateZ";
	rename -uid "D8944ED7-48BB-5B4B-66C1-76B2567C7C6B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.7758929636329412 170 1.545107807032764
		 180 0.4800977767445147 190 0.36893002688884735 200 0.4629381000995636 210 0.34179378999397159
		 220 0.38620488485321403 230 0.4523691488429904 240 0.50887573161162436 250 1.3976859161630273
		 260 1.7185894714202732 270 1.3252284843474627;
createNode animCurveTL -n "Character1_RightHandThumb1_translateX";
	rename -uid "E396138C-427F-6C61-4D83-E7A0E3B079D7";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.4003679156303406 170 0.69281235337257385
		 180 2.0311698317527771 190 1.6018308699131012 200 1.5143081545829773 210 1.5326008200645447
		 220 1.4818824827671051 230 1.3908237218856812 240 1.3794109225273132 250 1.5399746596813202
		 260 0.9378187358379364 270 2.0074412226676941;
createNode animCurveTL -n "Character1_RightHandThumb1_translateY";
	rename -uid "0B1E6B68-4A37-6025-732F-289B2B4E82B8";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 2.21661776304245 170 1.886710524559021
		 180 1.5765421092510223 190 1.544865220785141 200 1.2543931603431702 210 0.9999297559261322
		 220 0.98870694637298584 230 0.91760829091072083 240 0.90351775288581848 250 1.2579850852489471
		 260 1.7427384853363037 270 0.40888935327529907;
createNode animCurveTL -n "Character1_RightHandThumb1_translateZ";
	rename -uid "F97B4B41-464B-6DCD-7A56-5390A1177F5A";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.9776073863340571 170 0.84664838814205723
		 180 -0.96185386937577277 190 -1.0492596851236158 200 -0.96221940848408849 210 -0.88694126625341596
		 220 -0.77337882357824128 230 -0.69032387191327871 240 -0.72997520674107363 250 0.39929965059855022
		 260 0.28460940225158993 270 1.5465065909438636;
createNode animCurveTL -n "Character1_RightHand_translateX";
	rename -uid "FD4ACBBB-4514-461C-D877-869877114DF8";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 1.9569151103496552 170 3.4258581697940826
		 180 5.7602383196353912 190 6.1890877783298492 200 6.2641829252243042 210 6.6015422344207764
		 220 6.7791938781738281 230 6.9058209657669067 240 6.7798197269439697 250 6.5957307815551758
		 260 4.6353779733181 270 2.4183399975299835;
createNode animCurveTL -n "Character1_RightHand_translateY";
	rename -uid "7F225B39-4460-4D1C-65C3-CB93073E5AD4";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 -9.4596147537231445 170 13.043005764484406
		 180 16.812741011381149 190 16.49794802069664 200 16.811800003051758 210 16.916079819202423
		 220 17.272612452507019 230 17.32751727104187 240 17.04200953245163 250 15.244363993406296
		 260 10.229864716529846 270 -11.007311940193176;
createNode animCurveTL -n "Character1_RightHand_translateZ";
	rename -uid "344AFD72-4884-3D12-1095-AEAC33B0FBD8";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  160 20.172379899622683 170 4.6384745653995196
		 180 3.1174326577456668 190 4.5607776224187546 200 3.5692961167114845 210 2.1007834775446099
		 220 4.3547970137296943 230 3.4177923001152521 240 2.7971609588348656 250 1.3747201672231313
		 260 4.049980535683062 270 15.022211095515559;
createNode animCurveTL -n "Character1_RightForeArm_translateX";
	rename -uid "3B8F1931-4FFA-7DE8-0C79-84BA2786093C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -4.2735949158668518 20 -3.8845382630825043
		 30 -3.6261498928070068 40 -3.4343026578426361 50 -3.415583074092865 60 -3.65886390209198
		 70 -3.6401644349098206 80 -3.4642741084098816 90 -3.4336388111114502 100 -3.6361411213874817
		 110 -3.9848372340202332 120 -3.8318797945976257 130 -3.7785373628139496 140 -3.7672542035579681
		 150 -6.1394758522510529 160 -6.3782773911952972 170 -7.0246964693069458 180 -7.5824886560440063
		 190 -7.5079299509525299 200 -7.5518354773521423 210 -7.6520562171936035 220 -7.7106691896915436
		 230 -7.7891796827316284 240 -7.6595932245254517 250 -7.4994027614593506 260 -6.9900847971439362
		 270 -6.4409919083118439 280 -5.9861630201339722 290 -4.4779904186725616 300 -4.410727322101593
		 310 -4.8332378268241882 320 -4.7075450420379639 330 -4.3528139591217041 340 -4.4729344546794891
		 350 -4.4614322483539581 360 -4.3523579835891724 370 -4.2829535901546478 380 -4.1800372302532196
		 390 -4.2013540863990784 400 -4.1137866675853729;
createNode animCurveTL -n "Character1_RightForeArm_translateY";
	rename -uid "4AD0A58B-4A6D-6899-257E-C9923665A3F0";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -23.378576338291168 20 -22.971942275762558
		 30 -23.433367162942886 40 -23.53639081120491 50 -23.82735013961792 60 -23.655346781015396
		 70 -23.633258789777756 80 -23.891305178403854 90 -23.958773910999298 100 -23.510422557592392
		 110 -23.411592096090317 120 -23.904796689748764 130 -24.058279395103455 140 -24.459079653024673
		 150 -18.420501798391342 160 -20.471066236495972 170 -21.414586901664734 180 -21.038011461496353
		 190 -20.235011726617813 200 -20.266630500555038 210 -19.950145483016968 220 -20.093113929033279
		 230 -20.183631777763367 240 -20.335985720157623 250 -20.900630950927734 260 -22.084461897611618
		 270 -20.71717232465744 280 -20.575808733701706 290 -22.952301800251007 300 -22.617850452661514
		 310 -22.672690451145172 320 -22.580335289239883 330 -22.475823014974594 340 -22.330049425363541
		 350 -22.290871292352676 360 -22.353158891201019 370 -22.272035479545593 380 -22.361985594034195
		 390 -22.42651954293251 400 -22.5875124335289;
createNode animCurveTL -n "Character1_RightForeArm_translateZ";
	rename -uid "42A6266F-43C2-8747-CCA3-AF8CACDD4F5C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -6.5209193271584809 20 -8.1444671144708991
		 30 -8.0376344849355519 40 -8.3941847202368081 50 -7.8593862592242658 60 -7.7473600627854466
		 70 -8.6615259060636163 80 -9.0157516300678253 90 -8.0015057581476867 100 -8.7965406943112612
		 110 -8.5984944133087993 120 -7.4076976859942079 130 -8.7167312507517636 140 -7.3508329689502716
		 150 -11.167021945584565 160 -19.066469930112362 170 -3.0861122533679008 180 -0.74325688183307648
		 190 -1.9596235826611519 200 -0.79033160582184792 210 0.63574346713721752 220 -1.0229106992483139
		 230 -0.39276927709579468 240 -0.17124144360423088 250 0.53034592419862747 260 -2.8693660162389278
		 270 -13.988546608015895 280 -9.0692971833050251 290 -8.4275498986244202 300 -7.8972864663228393
		 310 -7.3214362026192248 320 -7.7418583212420344 330 -9.4129880424588919 340 -8.8117609731853008
		 350 -8.7616499746218324 360 -8.4536832757294178 370 -8.6452180054038763 380 -8.7634371360763907
		 390 -8.5500160697847605 400 -8.6987038375809789;
createNode animCurveTL -n "Character1_RightArm_translateX";
	rename -uid "2ADA6518-4685-0EED-2FF2-BA905517AA90";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -10.707 20 -10.707 30 -10.707 40 -10.707
		 50 -10.707 60 -10.707 70 -10.707 80 -10.707 90 -10.707 100 -10.707 110 -10.707 120 -10.707
		 130 -10.707 140 -10.707 150 -10.707 160 -10.707 170 -10.707 180 -10.707 190 -10.707
		 200 -10.707 210 -10.707 220 -10.707 230 -10.707 240 -10.707 250 -10.707 260 -10.707
		 270 -10.707 280 -10.707 290 -10.707 300 -10.707 310 -10.707 320 -10.707 330 -10.707
		 340 -10.707 350 -10.707 360 -10.707 370 -10.707 380 -10.707 390 -10.707 400 -10.707;
createNode animCurveTL -n "Character1_RightArm_translateY";
	rename -uid "721DF380-4F15-C45A-7358-CBB2E8308304";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 0 20 0 30 0 40 0 50 0 60 0 70 0 80 0
		 90 0 100 0 110 0 120 0 130 0 140 0 150 0 160 0 170 0 180 0 190 0 200 0 210 0 220 0
		 230 0 240 0 250 0 260 0 270 0 280 0 290 0 300 0 310 0 320 0 330 0 340 0 350 0 360 0
		 370 0 380 0 390 0 400 0;
createNode animCurveTL -n "Character1_RightArm_translateZ";
	rename -uid "48BF87E8-4A3D-AE92-6E8F-E0B1EF31DDA8";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 0 20 0 30 0 40 0 50 0 60 0 70 0 80 0
		 90 0 100 0 110 0 120 0 130 0 140 0 150 0 160 0 170 0 180 0 190 0 200 0 210 0 220 0
		 230 0 240 0 250 0 260 0 270 0 280 0 290 0 300 0 310 0 320 0 330 0 340 0 350 0 360 0
		 370 0 380 0 390 0 400 0;
createNode animCurveTA -n "Character1_RightArm_rotateX";
	rename -uid "29714B1A-4002-8E27-8436-42ADEE97E3CA";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 13.77 20 13.77 30 13.77 40 13.77 50 13.77
		 60 13.77 70 13.77 80 13.77 90 13.77 100 13.77 110 13.77 120 13.77 130 13.77 140 13.77
		 150 13.77 160 13.77 170 13.77 180 13.77 190 13.77 200 13.77 210 13.77 220 13.77 230 13.77
		 240 13.77 250 13.77 260 13.77 270 13.77 280 13.77 290 13.77 300 13.77 310 13.77 320 13.77
		 330 13.77 340 13.77 350 13.77 360 13.77 370 13.77 380 13.77 390 13.77 400 13.77;
createNode animCurveTA -n "Character1_RightArm_rotateY";
	rename -uid "61ECEA79-4092-03F1-DB9A-92B9D0B0AFBB";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 16.044 20 16.044 30 16.044 40 16.044
		 50 16.044 60 16.044 70 16.044 80 16.044 90 16.044 100 16.044 110 16.044 120 16.044
		 130 16.044 140 16.044 150 16.044 160 16.044 170 16.044 180 16.044 190 16.044 200 16.044
		 210 16.044 220 16.044 230 16.044 240 16.044 250 16.044 260 16.044 270 16.044 280 16.044
		 290 16.044 300 16.044 310 16.044 320 16.044 330 16.044 340 16.044 350 16.044 360 16.044
		 370 16.044 380 16.044 390 16.044 400 16.044;
createNode animCurveTA -n "Character1_RightArm_rotateZ";
	rename -uid "82926928-47E4-7077-916B-3D8FB103CA68";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 5.257 20 5.257 30 5.257 40 5.257 50 5.257
		 60 5.257 70 5.257 80 5.257 90 5.257 100 5.257 110 5.257 120 5.257 130 5.257 140 5.257
		 150 5.257 160 5.257 170 5.257 180 5.257 190 5.257 200 5.257 210 5.257 220 5.257 230 5.257
		 240 5.257 250 5.257 260 5.257 270 5.257 280 5.257 290 5.257 300 5.257 310 5.257 320 5.257
		 330 5.257 340 5.257 350 5.257 360 5.257 370 5.257 380 5.257 390 5.257 400 5.257;
createNode animCurveTL -n "Character1_LeftForeArm_translateX";
	rename -uid "05737DD7-43F9-3B6F-F267-26BF802BFC4B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 2.5216028094291687 20 2.3397088050842285
		 30 2.5538921356201172 40 2.3398026823997498 50 2.3655340075492859 60 2.4232238531112671
		 70 2.4739041924476624 80 2.3084521293640137 90 2.4568542838096619 100 2.6472106575965881
		 110 2.2839412093162537 120 2.4854868650436401 130 2.5340884923934937 140 2.5387287139892578
		 150 2.6188060641288757 160 2.8156086802482605 170 3.1418547034263611 180 3.0465424060821533
		 190 2.6810422539710999 200 2.7226477861404419 210 2.5720953941345215 220 2.595461905002594
		 230 2.6450201869010925 240 2.6504382491111755 250 2.5741294026374817 260 2.7238547801971436
		 270 3.0396446585655212 280 2.7116239070892334 290 2.9562324285507202 300 2.8958514332771301
		 310 2.9279306530952454 320 2.969639003276825 330 3.0219733715057373 340 3.0289024114608765
		 350 2.9560983180999756 360 2.8932094573974609 370 3.0080974102020264 380 2.8773441910743713
		 390 2.894572913646698 400 2.8720647096633911;
createNode animCurveTL -n "Character1_LeftForeArm_translateY";
	rename -uid "3A6F6FD2-4411-4D84-0927-1E8B163B6ADC";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -23.548371344804764 20 -24.090025573968887
		 30 -23.678306490182877 40 -23.928956687450409 50 -23.939846456050873 60 -24.080877006053925
		 70 -24.131906032562256 80 -24.411255866289139 90 -24.288824200630188 100 -24.253754317760468
		 110 -24.207222461700439 120 -24.232430756092072 130 -24.485403299331665 140 -24.631427228450775
		 150 -23.271464556455612 160 -24.619263410568237 170 -24.765846133232117 180 -24.795795232057571
		 190 -24.540122598409653 200 -24.909715354442596 210 -24.911025166511536 220 -24.952923506498337
		 230 -24.928560107946396 240 -24.847488105297089 250 -24.987208843231201 260 -25.010508298873901
		 270 -24.304836988449097 280 -24.1425521671772 290 -23.90989288687706 300 -24.000502377748489
		 310 -23.746304959058762 320 -23.846930265426636 330 -23.751425743103027 340 -23.617706447839737
		 350 -23.631546646356583 360 -23.93951341509819 370 -23.755846917629242 380 -23.806147277355194
		 390 -23.839250206947327 400 -23.885229974985123;
createNode animCurveTL -n "Character1_LeftForeArm_translateZ";
	rename -uid "7199C04A-46FE-F9F8-F120-38A21E4EABE0";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -6.9578627357259393 20 -6.7027466604486108
		 30 -6.9022022187709808 40 -7.2640368947759271 50 -7.4702483718283474 60 -6.9573700544424355
		 70 -7.4609520728699863 80 -7.8084167093038559 90 -7.0073229144327343 100 -7.0341034792363644
		 110 -6.8222339730709791 120 -7.4354044860228896 130 -7.4954480049200356 140 -6.9940975983627141
		 150 -5.8417472639121115 160 -9.2414521146565676 170 -8.997210580855608 180 -7.1694801561534405
		 190 -7.7967873774468899 200 -7.2004850953817368 210 -6.9980733096599579 220 -6.6409019753336906
		 230 -7.3791235685348511 240 -7.6592752709984779 250 -8.0051279626786709 260 -8.5298831574618816
		 270 -8.3054570015519857 280 -5.8565554674714804 290 -6.7872659827116877 300 -6.2765782931819558
		 310 -6.5802015597000718 320 -6.7796502728015184 330 -6.9808362051844597 340 -6.863840133883059
		 350 -6.575568113476038 360 -6.0814562486484647 370 -6.1816721688956022 380 -6.3630527816712856
		 390 -6.5699201775714755 400 -6.7028489895164967;
createNode animCurveTL -n "Character1_LeftArm_translateX";
	rename -uid "741BCD36-488B-3475-A8BB-35A5AB9C3F83";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 10.707 20 10.707 30 10.707 40 10.707
		 50 10.707 60 10.707 70 10.707 80 10.707 90 10.707 100 10.707 110 10.707 120 10.707
		 130 10.707 140 10.707 150 10.707 160 10.707 170 10.707 180 10.707 190 10.707 200 10.707
		 210 10.707 220 10.707 230 10.707 240 10.707 250 10.707 260 10.707 270 10.707 280 10.707
		 290 10.707 300 10.707 310 10.707 320 10.707 330 10.707 340 10.707 350 10.707 360 10.707
		 370 10.707 380 10.707 390 10.707 400 10.707;
createNode animCurveTL -n "Character1_LeftArm_translateY";
	rename -uid "525B099F-45CD-E268-79F9-CDAACC330979";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 0 20 0 30 0 40 0 50 0 60 0 70 0 80 0
		 90 0 100 0 110 0 120 0 130 0 140 0 150 0 160 0 170 0 180 0 190 0 200 0 210 0 220 0
		 230 0 240 0 250 0 260 0 270 0 280 0 290 0 300 0 310 0 320 0 330 0 340 0 350 0 360 0
		 370 0 380 0 390 0 400 0;
createNode animCurveTL -n "Character1_LeftArm_translateZ";
	rename -uid "6D9623B8-4E09-4F20-C183-08B155D652DC";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 0 20 0 30 0 40 0 50 0 60 0 70 0 80 0
		 90 0 100 0 110 0 120 0 130 0 140 0 150 0 160 0 170 0 180 0 190 0 200 0 210 0 220 0
		 230 0 240 0 250 0 260 0 270 0 280 0 290 0 300 0 310 0 320 0 330 0 340 0 350 0 360 0
		 370 0 380 0 390 0 400 0;
createNode animCurveTA -n "Character1_LeftArm_rotateX";
	rename -uid "BD2BAE02-4102-84F7-AD57-A98CF3671813";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -13.77 20 -13.77 30 -13.77 40 -13.77
		 50 -13.77 60 -13.77 70 -13.77 80 -13.77 90 -13.77 100 -13.77 110 -13.77 120 -13.77
		 130 -13.77 140 -13.77 150 -13.77 160 -13.77 170 -13.77 180 -13.77 190 -13.77 200 -13.77
		 210 -13.77 220 -13.77 230 -13.77 240 -13.77 250 -13.77 260 -13.77 270 -13.77 280 -13.77
		 290 -13.77 300 -13.77 310 -13.77 320 -13.77 330 -13.77 340 -13.77 350 -13.77 360 -13.77
		 370 -13.77 380 -13.77 390 -13.77 400 -13.77;
createNode animCurveTA -n "Character1_LeftArm_rotateY";
	rename -uid "930585C7-4561-8BF6-CBB2-8FA2B4FB3C9D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -16.044 20 -16.044 30 -16.044 40 -16.044
		 50 -16.044 60 -16.044 70 -16.044 80 -16.044 90 -16.044 100 -16.044 110 -16.044 120 -16.044
		 130 -16.044 140 -16.044 150 -16.044 160 -16.044 170 -16.044 180 -16.044 190 -16.044
		 200 -16.044 210 -16.044 220 -16.044 230 -16.044 240 -16.044 250 -16.044 260 -16.044
		 270 -16.044 280 -16.044 290 -16.044 300 -16.044 310 -16.044 320 -16.044 330 -16.044
		 340 -16.044 350 -16.044 360 -16.044 370 -16.044 380 -16.044 390 -16.044 400 -16.044;
createNode animCurveTA -n "Character1_LeftArm_rotateZ";
	rename -uid "C08BB6E5-4840-451F-8D96-8C9A0275C4EF";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 40 ".ktv[0:39]"  10 -5.257 20 -5.257 30 -5.257 40 -5.257
		 50 -5.257 60 -5.257 70 -5.257 80 -5.257 90 -5.257 100 -5.257 110 -5.257 120 -5.257
		 130 -5.257 140 -5.257 150 -5.257 160 -5.257 170 -5.257 180 -5.257 190 -5.257 200 -5.257
		 210 -5.257 220 -5.257 230 -5.257 240 -5.257 250 -5.257 260 -5.257 270 -5.257 280 -5.257
		 290 -5.257 300 -5.257 310 -5.257 320 -5.257 330 -5.257 340 -5.257 350 -5.257 360 -5.257
		 370 -5.257 380 -5.257 390 -5.257 400 -5.257;
select -ne :time1;
	setAttr ".o" 52;
	setAttr ".unw" 52;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".wsn" -type "string" "ACEScg";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "Character1_Hips.s" "Character1_LeftUpLeg.is";
connectAttr "Character1_LeftUpLeg.s" "Character1_LeftLeg.is";
connectAttr "Character1_LeftLeg.s" "Character1_LeftFoot.is";
connectAttr "Character1_LeftFoot.s" "Character1_LeftToeBase.is";
connectAttr "Character1_Hips.s" "Character1_RightUpLeg.is";
connectAttr "Character1_RightUpLeg.s" "Character1_RightLeg.is";
connectAttr "Character1_RightLeg.s" "Character1_RightFoot.is";
connectAttr "Character1_RightFoot.s" "Character1_RightToeBase.is";
connectAttr "Character1_Hips.s" "Character1_Spine.is";
connectAttr "Character1_Spine.s" "Character1_Spine1.is";
connectAttr "Character1_Spine1.s" "Character1_Spine2.is";
connectAttr "Character1_Spine2.s" "Character1_LeftShoulder.is";
connectAttr "Character1_LeftShoulder.s" "Character1_LeftArm.is";
connectAttr "Character1_LeftArm_translateX.o" "Character1_LeftArm.tx";
connectAttr "Character1_LeftArm_translateY.o" "Character1_LeftArm.ty";
connectAttr "Character1_LeftArm_translateZ.o" "Character1_LeftArm.tz";
connectAttr "Character1_LeftArm_rotateX.o" "Character1_LeftArm.rx";
connectAttr "Character1_LeftArm_rotateY.o" "Character1_LeftArm.ry";
connectAttr "Character1_LeftArm_rotateZ.o" "Character1_LeftArm.rz";
connectAttr "Character1_LeftArm.s" "Character1_LeftForeArm.is";
connectAttr "Character1_LeftForeArm_translateX.o" "Character1_LeftForeArm.tx";
connectAttr "Character1_LeftForeArm_translateY.o" "Character1_LeftForeArm.ty";
connectAttr "Character1_LeftForeArm_translateZ.o" "Character1_LeftForeArm.tz";
connectAttr "Character1_LeftForeArm.s" "Character1_LeftHand.is";
connectAttr "Character1_LeftHand.s" "Character1_LeftHandThumb1.is";
connectAttr "Character1_LeftHandThumb1.s" "Character1_LeftHandThumb2.is";
connectAttr "Character1_LeftHandThumb2.s" "Character1_LeftHandThumb3.is";
connectAttr "Character1_LeftHandThumb3.s" "Character1_LeftHandThumb4.is";
connectAttr "Character1_LeftHand.s" "Character1_LeftHandIndex1.is";
connectAttr "Character1_LeftHandIndex1.s" "Character1_LeftHandIndex2.is";
connectAttr "Character1_LeftHandIndex2.s" "Character1_LeftHandIndex3.is";
connectAttr "Character1_LeftHandIndex3.s" "Character1_LeftHandIndex4.is";
connectAttr "Character1_LeftHand.s" "Character1_LeftHandMiddle1.is";
connectAttr "Character1_LeftHandMiddle1.s" "Character1_LeftHandMiddle2.is";
connectAttr "Character1_LeftHandMiddle2.s" "Character1_LeftHandMiddle3.is";
connectAttr "Character1_LeftHandMiddle3.s" "Character1_LeftHandMiddle4.is";
connectAttr "Character1_LeftHand.s" "Character1_LeftHandRing1.is";
connectAttr "Character1_LeftHandRing1.s" "Character1_LeftHandRing2.is";
connectAttr "Character1_LeftHandRing2.s" "Character1_LeftHandRing3.is";
connectAttr "Character1_LeftHandRing3.s" "Character1_LeftHandRing4.is";
connectAttr "Character1_LeftHand.s" "Character1_LeftHandPinky1.is";
connectAttr "Character1_LeftHandPinky1.s" "Character1_LeftHandPinky2.is";
connectAttr "Character1_LeftHandPinky2.s" "Character1_LeftHandPinky3.is";
connectAttr "Character1_LeftHandPinky3.s" "Character1_LeftHandPinky4.is";
connectAttr "Character1_Spine2.s" "Character1_RightShoulder.is";
connectAttr "Character1_RightShoulder.s" "Character1_RightArm.is";
connectAttr "Character1_RightArm_translateX.o" "Character1_RightArm.tx";
connectAttr "Character1_RightArm_translateY.o" "Character1_RightArm.ty";
connectAttr "Character1_RightArm_translateZ.o" "Character1_RightArm.tz";
connectAttr "Character1_RightArm_rotateX.o" "Character1_RightArm.rx";
connectAttr "Character1_RightArm_rotateY.o" "Character1_RightArm.ry";
connectAttr "Character1_RightArm_rotateZ.o" "Character1_RightArm.rz";
connectAttr "Character1_RightArm.s" "Character1_RightForeArm.is";
connectAttr "Character1_RightForeArm_translateX.o" "Character1_RightForeArm.tx";
connectAttr "Character1_RightForeArm_translateY.o" "Character1_RightForeArm.ty";
connectAttr "Character1_RightForeArm_translateZ.o" "Character1_RightForeArm.tz";
connectAttr "Character1_RightForeArm.s" "Character1_RightHand.is";
connectAttr "Character1_RightHand_translateX.o" "Character1_RightHand.tx";
connectAttr "Character1_RightHand_translateY.o" "Character1_RightHand.ty";
connectAttr "Character1_RightHand_translateZ.o" "Character1_RightHand.tz";
connectAttr "Character1_RightHand.s" "Character1_RightHandThumb1.is";
connectAttr "Character1_RightHandThumb1_translateX.o" "Character1_RightHandThumb1.tx"
		;
connectAttr "Character1_RightHandThumb1_translateY.o" "Character1_RightHandThumb1.ty"
		;
connectAttr "Character1_RightHandThumb1_translateZ.o" "Character1_RightHandThumb1.tz"
		;
connectAttr "Character1_RightHandThumb1.s" "Character1_RightHandThumb2.is";
connectAttr "Character1_RightHandThumb2_translateX.o" "Character1_RightHandThumb2.tx"
		;
connectAttr "Character1_RightHandThumb2_translateY.o" "Character1_RightHandThumb2.ty"
		;
connectAttr "Character1_RightHandThumb2_translateZ.o" "Character1_RightHandThumb2.tz"
		;
connectAttr "Character1_RightHandThumb2.s" "Character1_RightHandThumb3.is";
connectAttr "Character1_RightHandThumb3_translateX.o" "Character1_RightHandThumb3.tx"
		;
connectAttr "Character1_RightHandThumb3_translateY.o" "Character1_RightHandThumb3.ty"
		;
connectAttr "Character1_RightHandThumb3_translateZ.o" "Character1_RightHandThumb3.tz"
		;
connectAttr "Character1_RightHandThumb3.s" "Character1_RightHandThumb4.is";
connectAttr "Character1_RightHandThumb4_translateX.o" "Character1_RightHandThumb4.tx"
		;
connectAttr "Character1_RightHandThumb4_translateY.o" "Character1_RightHandThumb4.ty"
		;
connectAttr "Character1_RightHandThumb4_translateZ.o" "Character1_RightHandThumb4.tz"
		;
connectAttr "Character1_RightHand.s" "Character1_RightHandIndex1.is";
connectAttr "Character1_RightHandIndex1_translateX.o" "Character1_RightHandIndex1.tx"
		;
connectAttr "Character1_RightHandIndex1_translateY.o" "Character1_RightHandIndex1.ty"
		;
connectAttr "Character1_RightHandIndex1_translateZ.o" "Character1_RightHandIndex1.tz"
		;
connectAttr "Character1_RightHandIndex1.s" "Character1_RightHandIndex2.is";
connectAttr "Character1_RightHandIndex2_translateX.o" "Character1_RightHandIndex2.tx"
		;
connectAttr "Character1_RightHandIndex2_translateY.o" "Character1_RightHandIndex2.ty"
		;
connectAttr "Character1_RightHandIndex2_translateZ.o" "Character1_RightHandIndex2.tz"
		;
connectAttr "Character1_RightHandIndex2.s" "Character1_RightHandIndex3.is";
connectAttr "Character1_RightHandIndex3_translateX.o" "Character1_RightHandIndex3.tx"
		;
connectAttr "Character1_RightHandIndex3_translateY.o" "Character1_RightHandIndex3.ty"
		;
connectAttr "Character1_RightHandIndex3_translateZ.o" "Character1_RightHandIndex3.tz"
		;
connectAttr "Character1_RightHandIndex3.s" "Character1_RightHandIndex4.is";
connectAttr "Character1_RightHandIndex4_translateX.o" "Character1_RightHandIndex4.tx"
		;
connectAttr "Character1_RightHandIndex4_translateY.o" "Character1_RightHandIndex4.ty"
		;
connectAttr "Character1_RightHandIndex4_translateZ.o" "Character1_RightHandIndex4.tz"
		;
connectAttr "Character1_RightHand.s" "Character1_RightHandMiddle1.is";
connectAttr "Character1_RightHandMiddle1_translateX.o" "Character1_RightHandMiddle1.tx"
		;
connectAttr "Character1_RightHandMiddle1_translateY.o" "Character1_RightHandMiddle1.ty"
		;
connectAttr "Character1_RightHandMiddle1_translateZ.o" "Character1_RightHandMiddle1.tz"
		;
connectAttr "Character1_RightHandMiddle1.s" "Character1_RightHandMiddle2.is";
connectAttr "Character1_RightHandMiddle2_translateX.o" "Character1_RightHandMiddle2.tx"
		;
connectAttr "Character1_RightHandMiddle2_translateY.o" "Character1_RightHandMiddle2.ty"
		;
connectAttr "Character1_RightHandMiddle2_translateZ.o" "Character1_RightHandMiddle2.tz"
		;
connectAttr "Character1_RightHandMiddle2.s" "Character1_RightHandMiddle3.is";
connectAttr "Character1_RightHandMiddle3_translateX.o" "Character1_RightHandMiddle3.tx"
		;
connectAttr "Character1_RightHandMiddle3_translateY.o" "Character1_RightHandMiddle3.ty"
		;
connectAttr "Character1_RightHandMiddle3_translateZ.o" "Character1_RightHandMiddle3.tz"
		;
connectAttr "Character1_RightHandMiddle3.s" "Character1_RightHandMiddle4.is";
connectAttr "Character1_RightHandMiddle4_translateX.o" "Character1_RightHandMiddle4.tx"
		;
connectAttr "Character1_RightHandMiddle4_translateY.o" "Character1_RightHandMiddle4.ty"
		;
connectAttr "Character1_RightHandMiddle4_translateZ.o" "Character1_RightHandMiddle4.tz"
		;
connectAttr "Character1_RightHand.s" "Character1_RightHandRing1.is";
connectAttr "Character1_RightHandRing1_translateX.o" "Character1_RightHandRing1.tx"
		;
connectAttr "Character1_RightHandRing1_translateY.o" "Character1_RightHandRing1.ty"
		;
connectAttr "Character1_RightHandRing1_translateZ.o" "Character1_RightHandRing1.tz"
		;
connectAttr "Character1_RightHandRing1.s" "Character1_RightHandRing2.is";
connectAttr "Character1_RightHandRing2_translateX.o" "Character1_RightHandRing2.tx"
		;
connectAttr "Character1_RightHandRing2_translateY.o" "Character1_RightHandRing2.ty"
		;
connectAttr "Character1_RightHandRing2_translateZ.o" "Character1_RightHandRing2.tz"
		;
connectAttr "Character1_RightHandRing2.s" "Character1_RightHandRing3.is";
connectAttr "Character1_RightHandRing3_translateX.o" "Character1_RightHandRing3.tx"
		;
connectAttr "Character1_RightHandRing3_translateY.o" "Character1_RightHandRing3.ty"
		;
connectAttr "Character1_RightHandRing3_translateZ.o" "Character1_RightHandRing3.tz"
		;
connectAttr "Character1_RightHandRing3.s" "Character1_RightHandRing4.is";
connectAttr "Character1_RightHandRing4_translateX.o" "Character1_RightHandRing4.tx"
		;
connectAttr "Character1_RightHandRing4_translateY.o" "Character1_RightHandRing4.ty"
		;
connectAttr "Character1_RightHandRing4_translateZ.o" "Character1_RightHandRing4.tz"
		;
connectAttr "Character1_RightHand.s" "Character1_RightHandPinky1.is";
connectAttr "Character1_RightHandPinky1_translateX.o" "Character1_RightHandPinky1.tx"
		;
connectAttr "Character1_RightHandPinky1_translateY.o" "Character1_RightHandPinky1.ty"
		;
connectAttr "Character1_RightHandPinky1_translateZ.o" "Character1_RightHandPinky1.tz"
		;
connectAttr "Character1_RightHandPinky1.s" "Character1_RightHandPinky2.is";
connectAttr "Character1_RightHandPinky2_translateX.o" "Character1_RightHandPinky2.tx"
		;
connectAttr "Character1_RightHandPinky2_translateY.o" "Character1_RightHandPinky2.ty"
		;
connectAttr "Character1_RightHandPinky2_translateZ.o" "Character1_RightHandPinky2.tz"
		;
connectAttr "Character1_RightHandPinky2.s" "Character1_RightHandPinky3.is";
connectAttr "Character1_RightHandPinky3_translateX.o" "Character1_RightHandPinky3.tx"
		;
connectAttr "Character1_RightHandPinky3_translateY.o" "Character1_RightHandPinky3.ty"
		;
connectAttr "Character1_RightHandPinky3_translateZ.o" "Character1_RightHandPinky3.tz"
		;
connectAttr "Character1_RightHandPinky3.s" "Character1_RightHandPinky4.is";
connectAttr "Character1_RightHandPinky4_translateX.o" "Character1_RightHandPinky4.tx"
		;
connectAttr "Character1_RightHandPinky4_translateY.o" "Character1_RightHandPinky4.ty"
		;
connectAttr "Character1_RightHandPinky4_translateZ.o" "Character1_RightHandPinky4.tz"
		;
connectAttr "Character1_Spine2.s" "Character1_Neck.is";
connectAttr "Character1_Neck.s" "Character1_Head.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "HIKproperties1.msg" "Character1.propertyState";
connectAttr "HIKSkeletonGeneratorNode1.CharacterNode" "Character1.SkeletonGenerator"
		;
connectAttr "Character1_Reference.ch" "Character1.Reference";
connectAttr "Character1_Hips.ch" "Character1.Hips";
connectAttr "Character1_LeftUpLeg.ch" "Character1.LeftUpLeg";
connectAttr "Character1_LeftLeg.ch" "Character1.LeftLeg";
connectAttr "Character1_LeftFoot.ch" "Character1.LeftFoot";
connectAttr "Character1_RightUpLeg.ch" "Character1.RightUpLeg";
connectAttr "Character1_RightLeg.ch" "Character1.RightLeg";
connectAttr "Character1_RightFoot.ch" "Character1.RightFoot";
connectAttr "Character1_Spine.ch" "Character1.Spine";
connectAttr "Character1_LeftArm.ch" "Character1.LeftArm";
connectAttr "Character1_LeftForeArm.ch" "Character1.LeftForeArm";
connectAttr "Character1_LeftHand.ch" "Character1.LeftHand";
connectAttr "Character1_RightArm.ch" "Character1.RightArm";
connectAttr "Character1_RightForeArm.ch" "Character1.RightForeArm";
connectAttr "Character1_RightHand.ch" "Character1.RightHand";
connectAttr "Character1_Head.ch" "Character1.Head";
connectAttr "Character1_LeftToeBase.ch" "Character1.LeftToeBase";
connectAttr "Character1_RightToeBase.ch" "Character1.RightToeBase";
connectAttr "Character1_LeftShoulder.ch" "Character1.LeftShoulder";
connectAttr "Character1_RightShoulder.ch" "Character1.RightShoulder";
connectAttr "Character1_Neck.ch" "Character1.Neck";
connectAttr "Character1_Spine1.ch" "Character1.Spine1";
connectAttr "Character1_Spine2.ch" "Character1.Spine2";
connectAttr "Character1_LeftHandThumb1.ch" "Character1.LeftHandThumb1";
connectAttr "Character1_LeftHandThumb2.ch" "Character1.LeftHandThumb2";
connectAttr "Character1_LeftHandThumb3.ch" "Character1.LeftHandThumb3";
connectAttr "Character1_LeftHandThumb4.ch" "Character1.LeftHandThumb4";
connectAttr "Character1_LeftHandIndex1.ch" "Character1.LeftHandIndex1";
connectAttr "Character1_LeftHandIndex2.ch" "Character1.LeftHandIndex2";
connectAttr "Character1_LeftHandIndex3.ch" "Character1.LeftHandIndex3";
connectAttr "Character1_LeftHandIndex4.ch" "Character1.LeftHandIndex4";
connectAttr "Character1_LeftHandMiddle1.ch" "Character1.LeftHandMiddle1";
connectAttr "Character1_LeftHandMiddle2.ch" "Character1.LeftHandMiddle2";
connectAttr "Character1_LeftHandMiddle3.ch" "Character1.LeftHandMiddle3";
connectAttr "Character1_LeftHandMiddle4.ch" "Character1.LeftHandMiddle4";
connectAttr "Character1_LeftHandRing1.ch" "Character1.LeftHandRing1";
connectAttr "Character1_LeftHandRing2.ch" "Character1.LeftHandRing2";
connectAttr "Character1_LeftHandRing3.ch" "Character1.LeftHandRing3";
connectAttr "Character1_LeftHandRing4.ch" "Character1.LeftHandRing4";
connectAttr "Character1_LeftHandPinky1.ch" "Character1.LeftHandPinky1";
connectAttr "Character1_LeftHandPinky2.ch" "Character1.LeftHandPinky2";
connectAttr "Character1_LeftHandPinky3.ch" "Character1.LeftHandPinky3";
connectAttr "Character1_LeftHandPinky4.ch" "Character1.LeftHandPinky4";
connectAttr "Character1_RightHandThumb1.ch" "Character1.RightHandThumb1";
connectAttr "Character1_RightHandThumb2.ch" "Character1.RightHandThumb2";
connectAttr "Character1_RightHandThumb3.ch" "Character1.RightHandThumb3";
connectAttr "Character1_RightHandThumb4.ch" "Character1.RightHandThumb4";
connectAttr "Character1_RightHandIndex1.ch" "Character1.RightHandIndex1";
connectAttr "Character1_RightHandIndex2.ch" "Character1.RightHandIndex2";
connectAttr "Character1_RightHandIndex3.ch" "Character1.RightHandIndex3";
connectAttr "Character1_RightHandIndex4.ch" "Character1.RightHandIndex4";
connectAttr "Character1_RightHandMiddle1.ch" "Character1.RightHandMiddle1";
connectAttr "Character1_RightHandMiddle2.ch" "Character1.RightHandMiddle2";
connectAttr "Character1_RightHandMiddle3.ch" "Character1.RightHandMiddle3";
connectAttr "Character1_RightHandMiddle4.ch" "Character1.RightHandMiddle4";
connectAttr "Character1_RightHandRing1.ch" "Character1.RightHandRing1";
connectAttr "Character1_RightHandRing2.ch" "Character1.RightHandRing2";
connectAttr "Character1_RightHandRing3.ch" "Character1.RightHandRing3";
connectAttr "Character1_RightHandRing4.ch" "Character1.RightHandRing4";
connectAttr "Character1_RightHandPinky1.ch" "Character1.RightHandPinky1";
connectAttr "Character1_RightHandPinky2.ch" "Character1.RightHandPinky2";
connectAttr "Character1_RightHandPinky3.ch" "Character1.RightHandPinky3";
connectAttr "Character1_RightHandPinky4.ch" "Character1.RightHandPinky4";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of skeleton2.ma
