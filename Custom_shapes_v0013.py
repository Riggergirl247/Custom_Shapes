#####################################################################
# Custom_Shapes_Tool
# Version: 1.30
# Author: Aashi Shukla
#--------------------------------------------------------------------
# A simple and easy to use script for replacing your already existing
# Ctrls with a Custom made 6one. Also contains 18 shape presets and 6
# Text presets. What makes this script unique is that you get the opt
# -ion for replacing with Text Ctrls as well. 
#---------------------------------------------------------------------
# To run this script, just paste this file in your Maya Scripts Direct
# -ory and in your Maya Script Editor, paste the following bit of code:
# import Custom_shapes_v0013
# reload(Custom_shapes_v0013)
# Custom_shapes_v0013.GUI()
# and Run!
######################################################################

import maya.cmds as cmds

def GUI():
	#kill already existing UI
	if cmds.window('custom_shape_changer_UI', exists=True):
		cmds.deleteUI('custom_shape_changer_UI')
	#create new window
	Win = cmds.window('custom_shape_changer_UI', wh=(200,300), sizeable=True, mnb=1, mxb=0)
	#mainLayout
	tabs = cmds.tabLayout(imh=5, imw=5)
	#defining tabs
	main_tab = cmds.formLayout(p=tabs)
	cmds.formLayout(main_tab, edit=True)
	text_tab = cmds.formLayout(p=tabs)
	cmds.formLayout(text_tab, edit=True)
	help_tab = cmds.formLayout(p=tabs)
	cmds.formLayout(help_tab, edit=True)
	#naimg the tabs
	cmds.tabLayout(tabs, edit=True, tabLabel=((main_tab,"Main"),(text_tab,"Text"),(help_tab,"Help")) )
	
	#_______main Layout within main tab____________
	clm1 = cmds.columnLayout(adj=1, p=main_tab)
	#custom_shape_change
	cmds.text(l='  Custom Shape Change:', al='left', font="boldLabelFont")
	cmds.rowColumnLayout(nc=2, adj=1, co=([1, "both", 5],[2,"both",5]), p= clm1)
	cus_shape = cmds.textField(editable=False)
	cmds.button(l='Load Custom', c=lambda x:load_cus(cus_shape))
	sel_shape = cmds.textField(editable=False)
	cmds.button(l='Load Required', c=lambda x:load_sel(sel_shape))
	cmds.setParent(clm1)
	cmds.separator(h=2, st='none')
	cmds.button(l='Change Shape', w=200, h=30, c= change_custom_shape)
	cmds.separator(st='in', h=10)
	#preset_shape_change
	cmds.text(l='  Shape Change Presets:', al='left', font="boldLabelFont")
	cmds.rowColumnLayout(nc=2, adj=1, p = clm1)
	cmds.optionMenuGrp("Control_Change_Menu")
	#Presets:
	cmds.menuItem('cube')
	cmds.menuItem('circle')
	cmds.menuItem('triangle')
	cmds.menuItem('Pyramid')
	cmds.menuItem('Diamond')
	cmds.menuItem('square')
	cmds.menuItem('Cross')
	cmds.menuItem('Plus')
	cmds.menuItem('Pin')
	cmds.menuItem('Aim')
	cmds.menuItem('COG')
	cmds.menuItem('Arrow')
	cmds.menuItem('Double Sided Arrow        ')
	cmds.menuItem('Four Sided Arrow')
	cmds.menuItem('Arrow on Ball')
	cmds.menuItem('Rotate Arrow')
	cmds.menuItem('Flower')
	cmds.menuItem('Locator')
	#button
	cmds.button(l="CHANGE", c= Basic_shape_presets)
	
	# ____________Text tab____________________________
	clm2 = cmds.rowColumnLayout(nc=1, p = text_tab)
	cmds.text(l= 'Advanced Text Presets:', al='left', font="boldLabelFont")
	cmds.separator(st='none', h=5)
	amb = cmds.rowColumnLayout(p=clm2, nc=2, co=([1,"both",3], [2,"both",3]))
	COG_Button = cmds.button(l="COG", w=107, c = Text_var_COG)
	cmds.button(l="GUI", w=107, c = Text_var_GUI)
	cmds.separator(st='none', h=3)
	cmds.separator(st='none', h=3)
	cmds.button(l="Rt", w=107, c = Text_var_Rt)
	cmds.button(l="Lf", w=107, c = Text_var_Lf)
	cmds.separator(st='none', h=3)
	cmds.separator(st='none', h=3)
	cmds.button(l="FK \ IK", w=107, c = Text_var_FKIK)
	cmds.button(l="Head", w=107, c = Text_var_Head)
	cmds.setParent(clm2)
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout(nc=2, adj=2, p=clm2)
	cmds.text(l= "Custom Text : ")
	custom_text = cmds.textField()
	cmds.rowColumnLayout(nc=2, adj=2, p=clm2, cw=([1, 80],[2,120]), cat = ([2,"right",10]) )
	cmds.separator(st='none')
	cmds.button(l= "Apply", w=40, po=True, c=lambda x:Custom_text_var(custom_text))
	
	# __________contents of the Help Tab__________________
	cmds.rowColumnLayout(p= help_tab)
	helpText = 'Custom Shape Changer Tool \n\nVersion: 1.30 \n\nby Aashi Shukla \n------------------------------\nHow to use: \n1. Load the Custom Shape. Make sure the custom shape has center pivot. \n2. Load the curves whose shape you want to change. \n3. Click on "SHAPE CHANGE" button. \n\n______________________________\n\nA lot of shapes like Pyramid, Diamond, Rotate Arrow, Arrow on Ball etc are already available in the Shape Preset Menu. Make sure to check them out!\n\n______________________________\n\nFor Text Shapes, skip to the Text tab. Here, you will find some pre-defined text shapes like COG, GUI etc as well as an option for adding Custom Text shapes as well. \n\n______________________________\n\nJust type the text, select the OG shape and click "Apply".\n\n______________________________\n\nI hope this tool proves to be useful asset in your Rigging Mania! \n\nReport any bugs at: aashi41207@gmail.com'
	cmds.scrollField( text = helpText, w=230, h=150, editable = False, wordWrap = True )
	# run the window
	cmds.showWindow(Win)
	
if __name__=="__main__":
	GUI()




""" 
      Functions used in GUI starts from here 
      
                                                  """
                                                  
                                                  
#========================================================================================
#____________________________ Text Shape Chnager ________________________________________
#========================================================================================
def Text_var_COG(*args):
	variable = 'COG'
	main_text_shape_changer(variable)

def Text_var_GUI(*args):
	variable = 'GUI'
	main_text_shape_changer(variable)
	
def Text_var_Rt(*args):
	variable = 'Rt'
	main_text_shape_changer(variable)

def Text_var_Lf(*args):
	variable = 'Lf'
	main_text_shape_changer(variable)

def Text_var_FKIK(*args):
	variable = 'FK\IK'
	main_text_shape_changer(variable)

def Text_var_Head(*args):
	variable = 'Head'
	main_text_shape_changer(variable)

def Custom_text_var(custom_text):
	variable = cmds.textField(custom_text, text=True, query=True)
	main_text_shape_changer(variable)

def main_text_shape_changer(variable):
	sel_list = cmds.ls(sl=True)
	var = variable
	cmds.textCurves(constructionHistory=False, t=var, font='Times New Roman')
	cmds.ungroup()
	cmds.ungroup()
	cmds.makeIdentity(apply=True, t=1, r=1, s=1)
	All_curves = cmds.ls(sl=True)
	Child_curves = All_curves[1:]
	cmds.select( Child_curves, r=True)
	cmds.pickWalk(d='down')
	cmds.select(All_curves[0], tgl=True)
	cmds.parent(r=True, s=True)
	cmds.pickWalk(d='up')
	main_control = cmds.ls(sl=True)[0]
	cmds.delete(Child_curves)
	cmds.rename(main_control, var)
	cmds.xform(cp=True)
	controller_formed = cmds.ls(sl=True)
	# exchange this controller with the previous one...
	i= 0
	for obj in sel_list:
		shape_node = cmds.listRelatives(cmds.duplicate(n=obj+str(i)))
		print shape_node
		cmds.delete(cmds.listRelatives(obj, s=True))
		cmds.select(shape_node, r=True)
		cmds.select(obj, tgl=True)
		cmds.parent(r=True, s=True)
		cmds.delete(obj+str(i))
	# delete the duplicate controller...
	cmds.pickWalk(d='up')
	cmds.delete(controller_formed)
	cmds.select(sel_list)

# --------------------------------------------------------------------------
# --------------- custom shape change --------------------------------------
# --------------------------------------------------------------------------

def load_cus(cus_shape):
	global custom_shape_list
	custom_shape_list = cmds.ls(sl=True)
	mgs = len(custom_shape_list)
	if mgs!=1:
		cmds.error('Please select only one custom shape', n=True)
	else:
		cmds.textField(cus_shape, e=1, text= custom_shape_list[0])

def load_sel(sel_shape):
	global selected_shape_list
	selected_shape_list = cmds.ls(sl=True)
	if len(selected_shape_list)<1:
		cmds.error('Select something!', n=True)
	cmds.textField(sel_shape, e=1, text= selected_shape_list[0])
	
def change_custom_shape(*args):
	global custom_shape_list
	global selected_shape_list
	print custom_shape_list, selected_shape_list
	i=0
	#command starts from here...
	for item in selected_shape_list:
		shape_node = cmds.listRelatives(cmds.duplicate(custom_shape_list, n = item + str(i)), s=True)
		print shape_node
		cmds.delete(cmds.listRelatives(item, s=True))
		cmds.parent(shape_node, item, r=True, s=True)
		cmds.select(cl=True)
		cmds.delete(item + str(i))
		i+=1
	cmds.select(selected_shape_list)
		
# ----------------------- Basic Shape Presets ------------------------------
def Basic_shape_presets(*args):
	n=1
	i=1
	selection_list = cmds.ls(sl=True)
	preset_shape = cmds.optionMenuGrp("Control_Change_Menu", query=True, value=True)
	#check if the selection sets are empty
	if len(selection_list)<1:
		cmds.error('Select something!', n=True)
	#loop through the selection...
	for item in selection_list:
		#create basic change shapes
		if preset_shape == 'cube':
			v = cmds.curve(n = item + str(i), d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), (-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n),(n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)])
			
		elif preset_shape == 'circle':
			v = cmds.circle(n = item + str(i))
			cmds.xform(item + str(i), ro=(90,0,0))
		
		elif preset_shape == 'triangle':
			v = cmds.curve(n= item + str(i), d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)])
		
		elif preset_shape == 'Pyramid':
			v = cmds.curve(n= item + str(i), d=1, p=[(0, 0, -1.25*n), (1.25*n, 0, 0), (0, 0, 1.25*n), (-1.25*n, 0, 0), (0, 0, -1.25*n), (0, 1.25*n, 0), (0, 0, 1.25*n), (1.25*n, 0 ,0), (0, 1.25*n, 0),(-1.25*n, 0 ,0 )])
			cmds.select(item + str(i) + '.cv[0]',item + str(i)+ '.cv[1]',item + str(i)+ '.cv[2]',item + str(i) + '.cv[3]',item + str(i) + '.cv[4]',item + str(i)+ '.cv[6]',item + str(i) + '.cv[7]',item + str(i) + '.cv[9]')
			cmds.scale( 0.6, 0.6, 0.6)
			cmds.xform(item + str(i), ro=(0,45,0))
			
		elif preset_shape == 'Diamond':
			v = cmds.curve(n= item + str(i), d=1, p =[(1.25*n,0, 0), (0, 0, -1.25*n), (-1.25*n, 0, 0), (0, 0, 1.25*n), (1.25*n, 0, 0), (0, 1.25*n, 0),  (-1.25*n, 0,0) ,(0, -1.25*n, 0), (1.25*n, 0, 0), (0, 0 ,1.25*n), (0, 1.25*n, 0), (0, 0, -1.25*n), (0, -1.25*n, 0), ( 0, 0 ,1.25*n)])
			cmds.xform(item + str(i) , ro=(0,45,0), s=(0.8, 0.8, 0.8))
			
		elif preset_shape == 'square':
			v = cmds.curve(n= item + str(i), d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
			
		elif preset_shape == 'Cross':
			v = cmds.curve(n= item + str(i), d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),(-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] )
			cmds.xform(item + str(i), s=(0.2, 0.2, 0.2), ro=(0,45,0))
			cmds.select(item + str(i) + '.cv[1:2]',item + str(i) + '.cv[4:5]',item + str(i) + '.cv[7:8]',item + str(i)+ '.cv[10:11]')
			cmds.scale(1.65, 1.65, 1.65)
			
		elif preset_shape == 'Plus':
			v = cmds.curve(n= item + str(i) , d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),(-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] )
			cmds.scale(0.25, 0.25, 0.25)
		
		elif preset_shape == 'Pin':
			cmds.circle(n=item + str(i) , d=3, radius=n)
			cmds.select(item + str(i) + '.cv[3:7]' )
			cmds.scale(0.02, 1, 1, r=True, ocp=True, xc= 'edge')
			cmds.select(item + str(i) + '.cv[0:2]')
			cmds.scale(0.414, 1, 1)
			
		elif preset_shape == 'Aim':
			v = cmds.curve(n= item + str(i), d=1, p= [(0, -1.25*n, 0), (0, 0, 0), (1.25*n, 0, 0), (0, 1.25*n, 0), (-1.25*n, 0, 0), (0, 0, 0), (0, 0, -1.25*n), (0, 1.25*n, 0) ,(0, 0, 1.25*n), (0, 0, 0), (0, 1.25*n ,0 )] )
		
		elif preset_shape == 'COG':
			v = cmds.circle( radius = n, n= item + str(i), ch=0)
			cmds.xform( item + str(i), ro=(-90,0,0), r=True, os=True)
			cmds.makeIdentity(item + str(i) , apply=True, t=1, r=1, s=1)
			# 2nd shape
			child_curve = cmds.curve(n= '_C1', d=1, p = [(-1.25*n, 0, -1.25*n), (-1.25*n, 0, -3.75*n), (-2.5*n, 0, -3.75*n), (0, 0, -6.25*n), (2.5*n, 0, -3.75*n), (1.25*n, 0, -3.75*n), (1.25*n, 0, -1.25*n),  (3.75*n, 0, -1.25*n), (3.75*n, 0, -2.5*n), (6.25*n, 0, 0),  (3.75*n, 0 ,2.5*n), (3.75*n, 0, 1.25*n), (1.25*n, 0 ,1.25*n), (1.25*n, 0, 3.75*n), (2.5*n, 0, 3.75*n),  (0, 0, 6.25*n), (-2.5*n, 0, 3.75*n),  (-1.25*n, 0, 3.75*n), (-1.25*n, 0, 1.25*n), (-3.75*n, 0, 1.25*n), (-3.75*n, 0 ,2.5*n), (-6.25*n, 0, 0), (-3.75*n, 0 ,-2.5*n), (-3.75*n, 0 ,-1.25*n), (-1.25*n, 0 ,-1.25*n)] )
			cmds.scale(0.35, 0.35, 0.35)
			cmds.select('_C1' + '.cv[0]', '_C1' + '.cv[6]', '_C1' + '.cv[12]', '_C1' + '.cv[18]', '_C1' + '.cv[24]' )
			cmds.scale( 2.4, 2.4, 2.4, r=True, ocp=True, xc='edge',a=True)
			cmds.makeIdentity(child_curve, apply=True, t=1, r=1, s=1)
			# combining the two shapes
			cmds.select( child_curve, r=True)
			cmds.pickWalk(d= 'down')
			cmds.select( v, tgl=True)
			cmds.parent(s=True, r=True)
			cmds.delete(child_curve)
			
		elif preset_shape == 'Arrow':
			m = n*0.25
			v = cmds.curve(n= item + str(i), d=1, p=[(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
		
		elif preset_shape == 'Double Sided Arrow        ':
			v = cmds.curve(n= item + str(i), d=1, p= [(-2.5*n, 0, -1.25*n), (2.5*n, 0, -1.25*n), (2.5*n, 0, -2.5*n) , (5*n, 0, 0), (2.5*n, 0, 2.5*n), (2.5*n, 0, 1.25*n), (-2.5*n, 0, 1.25*n), (-2.5*n, 0, 2.5*n), (-5*n, 0 ,0), (-2.5*n, 0, -2.5*n), (-2.5*n, 0, -1.25*n)] )
			cmds.scale(0.45, 0.45, 0.45)
		
		elif preset_shape == 'Four Sided Arrow':
			v = cmds.curve(n= item + str(i) , d=1, p = [(-1.25*n, 0, -1.25*n), (-1.25*n, 0, -3.75*n), (-2.5*n, 0, -3.75*n), (0, 0, -6.25*n), (2.5*n, 0, -3.75*n), (1.25*n, 0, -3.75*n), (1.25*n, 0, -1.25*n),  (3.75*n, 0, -1.25*n), (3.75*n, 0, -2.5*n), (6.25*n, 0, 0),  (3.75*n, 0 ,2.5*n), (3.75*n, 0, 1.25*n), (1.25*n, 0 ,1.25*n), (1.25*n, 0, 3.75*n), (2.5*n, 0, 3.75*n),  (0, 0, 6.25*n), (-2.5*n, 0, 3.75*n),  (-1.25*n, 0, 3.75*n), (-1.25*n, 0, 1.25*n), (-3.75*n, 0, 1.25*n), (-3.75*n, 0 ,2.5*n), (-6.25*n, 0, 0), (-3.75*n, 0 ,-2.5*n), (-3.75*n, 0 ,-1.25*n), (-1.25*n, 0 ,-1.25*n)] )
			cmds.scale(0.4, 0.4, 0.4)
			
		elif preset_shape == 'Arrow on Ball':
			v = cmds.curve(n= item + str(i), d=1, p= [(0,0.35, -1.00), (-0.336, 0.677, -0.751), (-0.0959, 0.677, -0.751), (-0.0959, 0.850, -0.500), ( -0.0959, 0.954, -0.0987),( -0.500, 0.850, -0.0987), (-0.751, 0.677, -0.0987) ,(-0.7511, 0.677, -0.336), ( -1.001567, 0.35,0 ),(-0.751, 0.677, 0.336), ( -0.751, 0.677, 0.0987), ( -0.500,0.8504, 0.0987),( -0.0959835, 0.954001 ,0.0987656), (-0.0959835, 0.850458, 0.500783), (-0.0959835, 0.677886, 0.751175), (-0.336638, 0.677886, 0.751175), (0, 0.35, 1.001567), (0.336638, 0.677886, 0.751175), (0.0959835, 0.677886, 0.751175), (0.0959835, 0.850458, 0.500783), ( 0.0959835, 0.954001, 0.0987656),(0.500783, 0.850458, 0.0987656) , (0.751175, 0.677886, 0.0987656), (0.751175, 0.677886, 0.336638), ( 1.001567, 0.35, 0 ), (0.751175, 0.677886 ,-0.336638), ( 0.751175, 0.677886, -0.0987656) , (0.500783, 0.850458 ,-0.0987656), (0.0959835, 0.954001, -0.0987656),(0.0959835, 0.850458, -0.500783), (0.0959835, 0.677886, -0.751175), (0.336638, 0.677886, -0.751175), (0, 0.35, -1.001567)] )
		
		elif preset_shape == 'Rotate Arrow':
			v = cmds.curve(n = item + str(i), d = 1, p= [(-0.124*n, 0, -1.096*n),  (-0.975*n, 0, -1.036*n),  (-0.559*n, 0 ,-0.944*n), (-0.798*n, 0 ,-0.798*n), (-1.042*n, 0, -0.431*n), (-1.128*n, 0, 0),  (-1.042*n, 0, 0.431*n), (-0.798*n, 0, 0.798*n),  (-0.560*n, 0, 0.946*n), (-0.975*n, 0, 1.036*n),  (-0.124*n, 0, 1.096*n), (-0.537*n, 0, 0.349*n), (-0.440*n, 0, 0.788*n),  (-0.652*n, 0, 0.652*n), (-0.853*n, 0, 0.353*n),  (-0.923*n, 0 ,0 ), (-0.853*n, 0, -0.353*n),  (-0.652*n, 0, -0.652*n), (-0.439*n, 0, -0.785*n),  (-0.537*n, 0 ,-0.349*n), (-0.124*n, 0, -1.096*n)] )
			cmds.xform(ro=(0,0,-90) )
			
		elif preset_shape == 'Flower':
			v = cmds.circle(n= item + str(i), radius=n*2, d=3, s=16)
			cmds.select(item + str(i) + '.cv[0]',item + str(i) + '.cv[2]',item + str(i) + '.cv[4]',item + str(i) + '.cv[6]',item + str(i) + '.cv[8]',item + str(i) + '.cv[10]',item + str(i) + '.cv[12]',item + str(i) + '.cv[14]')
			cmds.scale( 0.32,0.32,0.32)
			cmds.xform(item + str(i), ro=(90,0,0))
		
		elif preset_shape == 'Locator':
			v = cmds.curve(n= item + str(i), d=1, p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )
		
		else:
			cmds.error('Invalid option!', n=True)
			
		# Clear selection, select and clear history, freeze transforms
		cmds.select(cl=True)
		cmds.delete(item + str(i), constructionHistory=True)
		cmds.makeIdentity(item + str(i), apply=True, t=1, s=1, r=1)
		# Delete the shape node of item and parent the new shape node under the existing one and delete the dup transform node
		shape_node= cmds.listRelatives(item + str(i), s=True)
		
		cmds.delete(cmds.listRelatives(item, s=True))
		cmds.parent(shape_node, item, r=True, shape=True)
		cmds.delete(item + str(i))
		#pickwalk upwards since the shape node is still selected
		cmds.pickWalk(d='up')
	
	# select the entire list again
	cmds.select(selection_list)
# --------------------------------------------------------------------------
