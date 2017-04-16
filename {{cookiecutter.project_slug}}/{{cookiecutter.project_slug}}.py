## read plugin api:
## https://kupferlauncher.github.io/Documentation/PluginAPI.html

__kupfer_name__ = _('{{ cookiecutter.project_name }}')
__version__ = '{{ cookiecutter.version }}'
__author__ = '{{ cookiecutter.full_name.replace("\'", "\\\'") }} <{{ cookiecutter.email }}>'
__description__ = '''{{ cookiecutter.project_short_description }}'''

# # # optional:
# # # should be tuples of names of classes in the plugin
# __kupfer_sources__ = ("YourPluginSource",)
# __kupfer_actions__ = ("PluginActionName",)
# # # other options:
# __kupfer_text_sources__ = ("PLUGIN_TEXT_SOURCES",)
# __kupfer_action_generators__ = ("PLUGIN_ACTION_GENERATORS",)
# __kupfer_contents__ = ("PLUGIN_CONTENTS",)
#  
# # # if your plugin needs user settings
# from kupfer.plugin_support import PluginSettings
# __kupfer_settings__ = PluginSettings( 
#     {
#         "key" : "{{ cookiecutter.project_slug }}_KEY",
#         "label": _("SETTING_LABEL"),
#         "type": str,
#         "value": "SETTING_DEFAULT_VALUE",
#     }, 
# #     {
# #         "key" : "{{ cookiecutter.project_slug }}OTHER_KEY",
# #         "label": _("OTHER_SETTING_LABEL"),
# #         "type": int,
# #         "value": "OTHER_SETTING_DEFAULT_VALUE",
# #         "alternatives": OTHER_SETTING_LIST_OF_ALTERNATIVES
# #     },
# )
# # # then you can get setting:
# __kupfer_settings__["{{ cookiecutter.project_slug }}_KEY"]
#  
#  
# # # PLUGINS LEAFS
# # # leafs are plugin objects
# # # ie: TextLeaf, FileLeaf, ContactLeaf, EmailLeaf, FolderLeaf, ApplicationLeaf...
# from kupfer.objects import Leaf #, TextLeaf, FileLeaf, ContactLeaf, EmailLeaf, FolderLeaf, ApplicationLeaf
#  
#  
# class YourPluginLeaf(Leaf):
# #     #required
#     def __init__(self, obj):
#         Leaf.__init__(self, obj, _("Plugin Leaf Name"))
#  
# #     #optional
# #     #return list of actions that can work with this object
# #     def get_actions(self):
# #         yield Plugin_Action_name
#  
#  
# # # PLUGIN ACTIONS
# # # actions are what your plugin can do with objects
# # # ie: OpenFile, Delete, Edit, PlayNext...
# from kupfer.objects import Action
#  
#  
# class PluginActionName(Action):
# #     #required
#  
#     def __init__(self):
#         Action.__init__(self, name=_("Action Name"))
#  
#     def activate(self, leaf, iobj=None, ctx=None):
#         """Use this action with @obj and @iobj
#  
#         @leaf:  the direct object (Leaf)
#         @iobj: the indirect object (Leaf), if ``self.requires_object``
#                returns ``False``
#  
#         if ``self.wants_context`` returns ``True``, then the action
#         also receives an execution context object as ``ctx``.
#  
#         Also, ``activate_multiple(self, objects, iobjects=None, ctx=None)``
#         is called if it is defined and the action gets either
#         multiple objects or iobjects.
#         """
#         pass
#  
# #     #optional
# #     def wants_context(self):
# #         """Return ``True`` if ``activate`` should receive the
# #         ActionExecutionContext as the keyword argument context
# #  
# #         Defaults to ``False`` in accordance with the old protocol
# #         """
# #         return False
# #  
# #     def is_factory(self):
# #         """Return whether action may return a result collection as a Source"""
# #         return False
# #  
# #     def has_result(self):
# #         """Return whether action may return a result item as a Leaf"""
# #         return False
# #  
# #     def is_async(self):
# #         """If this action runs asynchronously, return True.
# #  
# #         Then activate(..) must return an object from the kupfer.task module,
# #         which will be queued to run by Kupfer's task scheduler.
# #         """
# #         return False
# #  
# #     def item_types(self):
# #         """Yield types this action may apply to. This is used only
# #         when this action is specified in __kupfer_actions__ to "decorate"
# #         """
# #         yield YourPluginLeaf
# #  
# #     def valid_for_item(self, item):
# #         """Whether action can be used with exactly @item"""
# #         return True
# #  
# #     def requires_object(self):
# #         """If this action requires a secondary object
# #         to complete is action, return True
# #         """
# #         return False
# #  
# #     def object_source(self, for_item=None):
# #         """Source to use for object or None,
# #         to use the catalog (flat and filtered for @object_types)
# #         """
# #         return None
# #  
# #     def object_types(self):
# #         """Yield types this action may use as indirect objects, if the action
# #         requrires it.
# #         """
# #         return ()
#  
#  
# # # PLUGIN_SOURCES
# # # source are leaf factory
# # # here is where kupfer will create your leafs
# # # ie: TextsSource, FilesSource, ContactsSource, ApplicationsSource...
# from kupfer.objects import Source
#  
#  
# class YourPluginSource(Source):
# #     #required
#     def __init__(self):
#         Source.__init__(self, _("Plugin Source Name"))
#         self.resource = None
#      
#     def get_items(self):
#         if self.resource:
#             for obj in []:
#                 yield YourPluginLeaf(obj)
#         raise StopIteration()
#      
# # #     #optional
# #     def initialize(self):
# #         """
# #         Called when a Source enters Kupfer's system for real
# #  
# #         This method is called at least once for any "real" Source. A Source
# #         must be able to return an icon name for get_icon_name as well as a
# #         description for get_description, even if this method was never called.
# #         """
# #         self.resource = None
# #  
# #     def finalize(self):
# #         """
# #         Called before a source is deactivated.
# #         """
# #         if self.resource:
# #             self.resource.finalize()
# #  
# #     def is_dynamic(self):
# #         """
# #         Whether to recompute contents each time it is accessed
# #         """
# #         return False
# #  
# #     def should_sort_lexically(self):
# #         """
# #         Sources should return items by most relevant order (most
# #         relevant first). If this is True, Source will sort items
# #         from get_item() in locale lexical order
# #         """
# #         return False
# #  
# #     def has_parent(self):
# #         return False
# #  
# #     def get_parent(self):
# #         return None
# #  
# #     def get_leaf_repr(self):
# #         """Return, if appicable, another object
# #         to take the source's place as Leaf"""
# #         return None
# #  
# #     def provides(self):
# #         """A seq of the types of items it provides;
# #         empty is taken as anything -- however most sources
# #         should set this to exactly the type they yield
# #         """
# #         return ()
