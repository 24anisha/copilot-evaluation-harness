import bpy
import itertools
from .. utils.timing import prettyTime
from .. utils.nodes import getAnimationNodeTrees

class OverviewPanel(bpy.types.Panel):
    bl_idname = "AN_PT_overview_panel"
    bl_label = "Overview"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Node Tree"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 2

    @classmethod
    def poll(cls, context):
        try: return context.space_data.node_tree.bl_idname == "an_AnimationNodeTree"
        except: return False

    def draw(self, context):
        layout = self.layout

        trees = getAnimationNodeTrees()

        col = layout.box().column(align = True)
        for tree in trees:
            row = col.row(align = True)
            row.operator("an.switch_tree", text = tree.name, emboss = False).treeName = tree.name
            row.label(text = prettyTime(tree.lastExecutionInfo.executionTime), icon = "TIME")

            icon = "LAYER_ACTIVE" if tree.autoExecution.enabled else "LAYER_USED"
            row.prop(tree.autoExecution, "enabled", icon = icon, text = "", icon_only = True)

        layout.operator("an.statistics_drawer", text = "Statistics", icon = "LINENUMBERS_ON")

        props = layout.operator("an.bake_to_keyframes", text = "Bake to Keyframes", icon = "DECORATE_KEYFRAME")
        props.startFrame = context.scene.frame_start
        props.endFrame = context.scene.frame_end