#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Tue Mar 31 23:24:36 2009

import wx

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        self.filePaths={}
        
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook = wx.Notebook(self, wx.NewId(), style=0)
        self.sequencePanel = wx.Panel(self.notebook, wx.NewId())
        self.dataPanel = wx.Panel(self.notebook, wx.NewId())
        self.mainPanel = wx.Panel(self.notebook, wx.NewId())
        self.newState = wx.Button(self.mainPanel, wx.NewId(), "New")
        self.openState = wx.Button(self.mainPanel, wx.NewId(), "Open")
        self.saveState = wx.Button(self.mainPanel, wx.NewId(), "Save")
        self.saveAsState = wx.Button(self.mainPanel, wx.NewId(), "Save as")
        self.exit = wx.Button(self.mainPanel, wx.NewId(), "Exit")
        self.help = wx.Button(self.mainPanel, wx.NewId(), "Help")
        self.fileList = wx.ListBox(self.dataPanel, wx.NewId(), choices=[],style=wx.LB_MULTIPLE)
        self.importFileList = wx.Button(self.dataPanel, wx.NewId(), "Import File List", style=wx.BU_LEFT)
        self.exportFileList = wx.Button(self.dataPanel, wx.NewId(), "Export File List", style=wx.BU_LEFT)
        self.addDBF = wx.Button(self.dataPanel, wx.NewId(), "Add DBF(s)", style=wx.BU_LEFT)
        self.addTobii = wx.Button(self.dataPanel, wx.NewId(), "Add Tobii TSV(s)", style=wx.BU_LEFT)
        self.addAnimeye = wx.Button(self.dataPanel, wx.NewId(), "Add Animeye TSV(s)", style=wx.BU_LEFT)
        self.removeFiles = wx.Button(self.dataPanel, wx.NewId(), "Remove File(s)", style=wx.BU_LEFT)
        self.selectAllFiles = wx.Button(self.dataPanel, wx.NewId(), "Select All", style=wx.BU_LEFT)
        self.inverseFileSelection = wx.Button(self.dataPanel, wx.NewId(), "Inverse Selection", style=wx.BU_LEFT)
        self.filterTypeLabel = wx.StaticText(self.dataPanel, wx.NewId(), "filter type", style=wx.ALIGN_CENTRE)
        self.filterFieldLabel = wx.StaticText(self.dataPanel, wx.NewId(), "field", style=wx.ALIGN_CENTRE)
        self.filterComparisonLabel = wx.StaticText(self.dataPanel, wx.NewId(), "comparison", style=wx.ALIGN_CENTRE)
        self.filterValueLabel = wx.StaticText(self.dataPanel, wx.NewId(), "value", style=wx.ALIGN_CENTRE)
        self.filterType = wx.ComboBox(self.dataPanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.filterField = wx.ComboBox(self.dataPanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.filterComparison = wx.ComboBox(self.dataPanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.filterValue = wx.TextCtrl(self.dataPanel, wx.NewId(), "")
        self.newFilterSpacer = wx.StaticText(self.dataPanel, wx.NewId(), "")
        self.createFilter = wx.Button(self.dataPanel, wx.NewId(), "Create Filter", style=wx.BU_LEFT)
        self.filterList = wx.ListBox(self.dataPanel, wx.NewId(), choices=[])
        self.importFilterList = wx.Button(self.dataPanel, wx.NewId(), "Import Filter List", style=wx.BU_LEFT)
        self.exportFilterList = wx.Button(self.dataPanel, wx.NewId(), "Export Filter List", style=wx.BU_LEFT)
        self.removeFilters = wx.Button(self.dataPanel, wx.NewId(), "Remove Filter(s)", style=wx.BU_LEFT)
        self.selectAllFilters = wx.Button(self.dataPanel, wx.NewId(), "Select All", style=wx.BU_LEFT)
        self.inverseFilterSelection = wx.Button(self.dataPanel, wx.NewId(), "Inverse Selection", style=wx.BU_LEFT)
        self.sequenceIDlabel = wx.StaticText(self.sequencePanel, wx.NewId(), "ID Field", style=wx.ALIGN_CENTRE)
        self.sortFieldLabel = wx.StaticText(self.sequencePanel, wx.NewId(), "Sort Field", style=wx.ALIGN_CENTRE)
        self.scaleFieldLabel = wx.StaticText(self.sequencePanel, wx.NewId(), "Scale Field", style=wx.ALIGN_CENTRE)
        self.AOIfieldLabel = wx.StaticText(self.sequencePanel, wx.NewId(), "AOI Field", style=wx.ALIGN_CENTRE)
        self.populateFields = wx.Button(self.sequencePanel, wx.NewId(), "Populate Fields", style=wx.BU_LEFT)
        self.sequenceID = wx.ComboBox(self.sequencePanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.sortField = wx.ComboBox(self.sequencePanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.scaleField = wx.ComboBox(self.sequencePanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.AOIfield = wx.ComboBox(self.sequencePanel, wx.NewId(), choices=[], style=wx.CB_DROPDOWN)
        self.autoselect = wx.Button(self.sequencePanel, wx.NewId(), "Auto Select", style=wx.BU_LEFT)
        self.AOIcode = wx.ListCtrl(self.sequencePanel, wx.NewId(), style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.importAOIcodeTable = wx.Button(self.sequencePanel, wx.NewId(), "Import Table", style=wx.BU_LEFT)
        self.exportAOIcodeTable = wx.Button(self.sequencePanel, wx.NewId(), "Export Table", style=wx.BU_LEFT)
        self.autoCodeAOI = wx.Button(self.sequencePanel, wx.NewId(), "Auto Code", style=wx.BU_LEFT)
        self.contextCodeAOI = wx.Button(self.sequencePanel, wx.NewId(), "Context Code", style=wx.BU_LEFT)
        self.saveSequence = wx.Button(self.sequencePanel, wx.NewId(), "Save Sequence", style=wx.BU_LEFT)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        wx.EVT_BUTTON(self,self.newState.GetId(),self.OnnewState)
        wx.EVT_BUTTON(self,self.openState.GetId(),self.OnopenState)
        wx.EVT_BUTTON(self,self.saveState.GetId(),self.OnsaveState)
        wx.EVT_BUTTON(self,self.saveAsState.GetId(),self.OnsaveAsState)
        wx.EVT_BUTTON(self,self.exit.GetId(),self.Onexit)
        wx.EVT_BUTTON(self,self.help.GetId(),self.Onhelp)
        wx.EVT_BUTTON(self,self.importFileList.GetId(),self.OnimportFileList)
        wx.EVT_BUTTON(self,self.exportFileList.GetId(),self.OnexportFileList)
        wx.EVT_BUTTON(self,self.addDBF.GetId(),self.OnaddDBF)
        wx.EVT_BUTTON(self,self.addTobii.GetId(),self.OnaddTobii)
        wx.EVT_BUTTON(self,self.addAnimeye.GetId(),self.OnaddAnimeye)
        wx.EVT_BUTTON(self,self.removeFiles.GetId(),self.OnremoveFiles)
        wx.EVT_BUTTON(self,self.selectAllFiles.GetId(),self.OnselectAllFiles)
        wx.EVT_BUTTON(self,self.inverseFileSelection.GetId(),self.OninverseFileSelection)
        wx.EVT_BUTTON(self,self.createFilter.GetId(),self.OncreateFilter)
        wx.EVT_BUTTON(self,self.importFilterList.GetId(),self.OnimportFilterList)
        wx.EVT_BUTTON(self,self.exportFilterList.GetId(),self.OnexportFilterList)
        wx.EVT_BUTTON(self,self.removeFilters.GetId(),self.OnremoveFilters)
        wx.EVT_BUTTON(self,self.selectAllFilters.GetId(),self.OnselectAllFilters)
        wx.EVT_BUTTON(self,self.inverseFilterSelection.GetId(),self.OninverseFilterSelection)
        wx.EVT_BUTTON(self,self.populateFields.GetId(),self.OnpopulateFields)
        wx.EVT_BUTTON(self,self.autoselect.GetId(),self.Onautoselect)
        wx.EVT_BUTTON(self,self.importAOIcodeTable.GetId(),self.OnimportAOIcodeTable)
        wx.EVT_BUTTON(self,self.exportAOIcodeTable.GetId(),self.OnexportAOIcodeTable)
        wx.EVT_BUTTON(self,self.autoCodeAOI.GetId(),self.OnautoCodeAOI)
        wx.EVT_BUTTON(self,self.contextCodeAOI.GetId(),self.OncontextCodeAOI)
        wx.EVT_BUTTON(self,self.saveSequence.GetId(),self.OnsaveSequence)
        

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Point Pattern Analyst")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        sequenceSizer = wx.BoxSizer(wx.VERTICAL)
        AOIcodeSizer = wx.BoxSizer(wx.HORIZONTAL)
        AOIcodeButtonSizer = wx.BoxSizer(wx.VERTICAL)
        sequenceFieldSizerSizer = wx.BoxSizer(wx.HORIZONTAL)
        sequenceFieldSizer = wx.BoxSizer(wx.HORIZONTAL)
        sequenceFieldLabelSizerSizer = wx.BoxSizer(wx.HORIZONTAL)
        sequenceFieldLabelSizer = wx.BoxSizer(wx.HORIZONTAL)
        dataSizer = wx.BoxSizer(wx.VERTICAL)
        filterSizer = wx.BoxSizer(wx.HORIZONTAL)
        filterButtonSizer = wx.BoxSizer(wx.VERTICAL)
        newFilterSizer = wx.BoxSizer(wx.HORIZONTAL)
        newFilterButtonSizer = wx.BoxSizer(wx.VERTICAL)
        newFilterFieldSizer = wx.BoxSizer(wx.VERTICAL)
        newFilterValueSizer = wx.BoxSizer(wx.HORIZONTAL)
        newFilterFieldLabelSizer = wx.BoxSizer(wx.HORIZONTAL)
        fileSizer = wx.BoxSizer(wx.HORIZONTAL)
        fileButtonSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.newState, 0, wx.EXPAND, 0)
        mainSizer.Add(self.openState, 0, wx.EXPAND, 0)
        mainSizer.Add(self.saveState, 0, wx.EXPAND, 0)
        mainSizer.Add(self.saveAsState, 0, wx.EXPAND, 0)
        mainSizer.Add(self.exit, 0, wx.EXPAND, 0)
        mainSizer.Add(self.help, 0, wx.EXPAND, 0)
        self.mainPanel.SetSizer(mainSizer)
        fileSizer.Add(self.fileList, 5, wx.EXPAND, 0)
        fileButtonSizer.Add(self.importFileList, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.exportFileList, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.addDBF, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.addTobii, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.addAnimeye, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.removeFiles, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.selectAllFiles, 0, wx.EXPAND, 0)
        fileButtonSizer.Add(self.inverseFileSelection, 0, wx.EXPAND, 0)
        fileSizer.Add(fileButtonSizer, 1, wx.EXPAND, 0)
        dataSizer.Add(fileSizer, 3, wx.ALL|wx.EXPAND, 1)
        newFilterFieldLabelSizer.Add(self.filterTypeLabel, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        newFilterFieldLabelSizer.Add(self.filterFieldLabel, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        newFilterFieldLabelSizer.Add(self.filterComparisonLabel, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        newFilterFieldLabelSizer.Add(self.filterValueLabel, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        newFilterFieldSizer.Add(newFilterFieldLabelSizer, 0, wx.EXPAND, 0)
        newFilterValueSizer.Add(self.filterType, 1, 0, 0)
        newFilterValueSizer.Add(self.filterField, 1, 0, 0)
        newFilterValueSizer.Add(self.filterComparison, 1, 0, 0)
        newFilterValueSizer.Add(self.filterValue, 1, 0, 0)
        newFilterFieldSizer.Add(newFilterValueSizer, 0, wx.EXPAND, 0)
        newFilterSizer.Add(newFilterFieldSizer, 5, wx.EXPAND, 0)
        newFilterButtonSizer.Add(self.newFilterSpacer, 0, 0, 0)
        newFilterButtonSizer.Add(self.createFilter, 0, wx.EXPAND, 0)
        newFilterSizer.Add(newFilterButtonSizer, 1, wx.EXPAND, 0)
        dataSizer.Add(newFilterSizer, 0, wx.ALL|wx.EXPAND, 1)
        filterSizer.Add(self.filterList, 5, wx.EXPAND, 0)
        filterButtonSizer.Add(self.importFilterList, 0, wx.EXPAND, 0)
        filterButtonSizer.Add(self.exportFilterList, 0, wx.EXPAND, 0)
        filterButtonSizer.Add(self.removeFilters, 0, wx.EXPAND, 0)
        filterButtonSizer.Add(self.selectAllFilters, 0, wx.EXPAND, 0)
        filterButtonSizer.Add(self.inverseFilterSelection, 0, wx.EXPAND, 0)
        filterSizer.Add(filterButtonSizer, 1, wx.EXPAND, 0)
        dataSizer.Add(filterSizer, 3, wx.TOP|wx.EXPAND, 5)
        self.dataPanel.SetSizer(dataSizer)
        sequenceFieldLabelSizer.Add(self.sequenceIDlabel, 1, wx.ALIGN_BOTTOM, 0)
        sequenceFieldLabelSizer.Add(self.sortFieldLabel, 1, wx.ALIGN_BOTTOM, 0)
        sequenceFieldLabelSizer.Add(self.scaleFieldLabel, 1, wx.ALIGN_BOTTOM, 0)
        sequenceFieldLabelSizer.Add(self.AOIfieldLabel, 1, wx.ALIGN_BOTTOM, 0)
        sequenceFieldLabelSizerSizer.Add(sequenceFieldLabelSizer, 5, wx.EXPAND, 0)
        sequenceFieldLabelSizerSizer.Add(self.populateFields, 1, 0, 0)
        sequenceSizer.Add(sequenceFieldLabelSizerSizer, 0, wx.EXPAND, 0)
        sequenceFieldSizer.Add(self.sequenceID, 1, 0, 0)
        sequenceFieldSizer.Add(self.sortField, 1, 0, 0)
        sequenceFieldSizer.Add(self.scaleField, 1, 0, 0)
        sequenceFieldSizer.Add(self.AOIfield, 1, 0, 0)
        sequenceFieldSizerSizer.Add(sequenceFieldSizer, 5, wx.EXPAND, 0)
        sequenceFieldSizerSizer.Add(self.autoselect, 1, 0, 0)
        sequenceSizer.Add(sequenceFieldSizerSizer, 0, wx.EXPAND, 0)
        AOIcodeSizer.Add(self.AOIcode, 5, wx.EXPAND, 0)
        AOIcodeButtonSizer.Add(self.importAOIcodeTable, 0, wx.EXPAND, 0)
        AOIcodeButtonSizer.Add(self.exportAOIcodeTable, 0, wx.EXPAND, 0)
        AOIcodeButtonSizer.Add(self.autoCodeAOI, 0, wx.EXPAND, 0)
        AOIcodeButtonSizer.Add(self.contextCodeAOI, 0, wx.EXPAND, 0)
        AOIcodeButtonSizer.Add(self.saveSequence, 0, wx.EXPAND, 0)
        AOIcodeSizer.Add(AOIcodeButtonSizer, 1, wx.EXPAND, 0)
        sequenceSizer.Add(AOIcodeSizer, 1, wx.ALL|wx.EXPAND, 3)
        self.sequencePanel.SetSizer(sequenceSizer)
        self.notebook.AddPage(self.mainPanel, "Main Menu")
        self.notebook.AddPage(self.dataPanel, "Data Selection and Filtering")
        self.notebook.AddPage(self.sequencePanel, "Sequence Creation")
        mainsizer.Add(self.notebook, 1, wx.EXPAND, 0)
        self.SetSizer(mainsizer)
        mainsizer.Fit(self)
        self.Layout()
        # end wxGlade

    def OnDevelopment(self, event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    #event helper functions
    #multiple add file dialog
    def OnAdd(self,listbox,paths,wcd):
        dialog = wx.FileDialog(self, message='Select files', wildcard=wcd, style=wx.MULTIPLE)
        temp=[]
        if dialog.ShowModal() == wx.ID_OK:
            temp= dialog.GetPaths()
        dialog.Destroy()
        for p in temp:
            name=p[p.rfind("\\")+1:]
            if not paths.has_key(name):
                paths[name]=p
                listbox.Insert(name,0)

    #multiple delete function
    def OnDel(self,listbox,paths):
        loc=list(listbox.GetSelections())
        loc.reverse()
        for l in loc:
            paths.pop(listbox.GetString(l))
            listbox.Delete(l)

    def OnnewState(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnopenState(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnsaveState(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnsaveAsState(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def Onexit(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def Onhelp(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnimportFileList(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnexportFileList(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnaddDBF(self,event):
        self.OnAdd(self.fileList,self.filePaths,"Data File (*.dbf)|*.dbf|All files (*.*)|*.*")

    def OnaddTobii(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnaddAnimeye(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnremoveFiles(self,event):
        self.OnDel(self.fileList,self.filePaths) 

    def OnselectAllFiles(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OninverseFileSelection(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OncreateFilter(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnimportFilterList(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnexportFilterList(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnremoveFilters(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnselectAllFilters(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OninverseFilterSelection(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnpopulateFields(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def Onautoselect(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnimportAOIcodeTable(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnexportAOIcodeTable(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnautoCodeAOI(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OncontextCodeAOI(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  

    def OnsaveSequence(self,event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)  


# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    mainframe = MyFrame(None, -1, "")
    app.SetTopWindow(mainframe)
    mainframe.Show()
    app.MainLoop()