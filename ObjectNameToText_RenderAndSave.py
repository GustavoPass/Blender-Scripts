import bpy

#----- Display selected object name on Text Object

selected_obj = bpy.context.object

#--Object name
#obj_name = selected_obj.name

#--Mesh data name
obj_name = selected_obj.data.name

txt = bpy.data.objects["Text"]
txt.data.body = obj_name

#----- Render and save

imageName = "render1.png"
savePath = "D:\Folder1\Folder2\Folder3\{}".format(imageName)

bpy.context.scene.render.filepath = savePath
bpy.ops.render.render(write_still=True)