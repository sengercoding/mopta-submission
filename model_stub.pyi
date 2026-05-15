from aimmspy.model.identifiers.set import Set
from aimmspy.model.identifiers.parameter import Parameter, NumericParameter, StringParameter, ElementParameter
from aimmspy.model.identifiers.variable import Variable
from aimmspy.model.identifiers.index import Index
from aimmspy.model.identifiers.constraint import Constraint
from aimmspy.model.identifiers.mathematical_program import MathematicalProgram
from aimmspy.model.procedure import Procedure
from aimmspy.model.module import Module
from aimmspy.model.library import AimmsLibrary
import pyarrow
class Model:
    def multi_assign(self, data : pyarrow.Table): ...
    def multi_data(self, identifiers: list[str]) -> pyarrow.Table: ...
    class pro:
        FileSeparator : StringParameter = ...
        """
"""
        PROMFLAG_ACK : NumericParameter = ...
        """
"""
        PROMFLAG_PRIORITY : NumericParameter = ...
        """
"""
        PROMFLAG_SYNC_ONLY : NumericParameter = ...
        """
"""
        PROMFLAG_LIVE : NumericParameter = ...
        """
"""
        PROMFLAG_REQUEST : NumericParameter = ...
        """
"""
        PROMFLAG_RESPONSE : NumericParameter = ...
        """
"""
        PROMFLAG_ERROR : NumericParameter = ...
        """
"""
        PROMFLAG_SESSION : NumericParameter = ...
        """
"""
        PROMFLAG_USER : NumericParameter = ...
        """
"""
        PROTS_CREATED : NumericParameter = ...
        """
Worker created but project not opened yet

"""
        PROTS_QUEUED : NumericParameter = ...
        """
Project opening requested and being executed

"""
        PROTS_INITIALIZING : NumericParameter = ...
        """
Project opening requested and being executed

"""
        PROTS_READY : NumericParameter = ...
        """
Waiting for new tasks to be executed

"""
        PROTS_RUNNING : NumericParameter = ...
        """
Running a task

"""
        PROTS_CLOSING : NumericParameter = ...
        """
Project closing; no more tasks will be handled

"""
        PROTS_FINISHED : NumericParameter = ...
        """
Project closed; no more tasks will be handled

"""
        PROTS_TERMINATED : NumericParameter = ...
        """
Project terminated during execution; no more tasks will be handled

"""
        PROTS_ERROR : NumericParameter = ...
        """
Project ended with an error; no more tasks will be handled

"""
        PROTS_DELETED : NumericParameter = ...
        """
Project ended with an error; no more tasks will be handled

"""
        AIMMSAPI_INTERRUPT_EXECUTE : NumericParameter = ...
        """
Interrupt the current running procedure

"""
        AIMMSAPI_INTERRUPT_SOLVE : NumericParameter = ...
        """
Interrupt the current solve statement

"""
        PROA_ADMIN_GROUP : NumericParameter = ...
        """
"""
        GetCurrentUserInfo : Procedure = ...
        """
"""
        DebugServerSession : NumericParameter = ...
        """
"""
        DeveloperModeDelegation : NumericParameter = ...
        """
0 = ask, 1 = delegate always, 2 = always solve locally

"""
        DefaultRequestDescription : StringParameter = ...
        """
"""
        DelegateToServer : Procedure = ...
        """
"""
        DelegateToNewSession : Procedure = ...
        """
"""
        DelegateToCurrentSession : Procedure = ...
        """
"""
        DelegateToClient : Procedure = ...
        """
"""
        DelegateToPeer : Procedure = ...
        """
"""
        GetObjectVersion : Procedure = ...
        """
"""
        GetObjectVersionDirect : Procedure = ...
        """
"""
        LoadLogMessages : Procedure = ...
        """
"""
        LoadCaseFromObjectVersion : Procedure = ...
        """
"""
        SupportsFeature : Procedure = ...
        """
"""
        GetVersionFullInfo : Procedure = ...
        """
"""
        SaveVersionInFolder : Procedure = ...
        """
"""
        SetDefaultRequestDescription : Procedure = ...
        """
"""
        SaveServerSideLog : Procedure = ...
        """
"""
        RetrieveServerSideLog : Procedure = ...
        """
"""
        SaveFileToCentralStorage : Procedure = ...
        """
"""
        RetrieveFileFromCentralStorage : Procedure = ...
        """
"""
        CreateStorageFolder : Procedure = ...
        """
"""
        DeleteStorageFolder : Procedure = ...
        """
"""
        DeleteStorageFile : Procedure = ...
        """
"""
        NormalizeStoragePath : Procedure = ...
        """
"""
        SplitStoragePath : Procedure = ...
        """
"""
        GetPROVersion : Procedure = ...
        """
"""
        PROUserFullname : StringParameter = ...
        """
"""
        CommandLineArguments : Set = ...
        """
"""
        ReadArguments : StringParameter = ...
        """
@index domain: (CL)

@unit:
"""
        PROConfigFile : StringParameter = ...
        """
"""
        PROEnvironment : StringParameter = ...
        """
"""
        PROUserName : StringParameter = ...
        """
"""
        PROUserEmail : StringParameter = ...
        """
"""
        PROPassword : StringParameter = ...
        """
"""
        PROUserGroups : Set = ...
        """
"""
        PROUserGroupName : StringParameter = ...
        """
@index domain: (userGroup)

@unit:
"""
        PROLastUserName : StringParameter = ...
        """
"""
        PROLogConfigFile : StringParameter = ...
        """
"""
        PROTempFolder : StringParameter = ...
        """
"""
        PROEndPoint : StringParameter = ...
        """
"""
        PROSessionTypes : Set = ...
        """
"""
        PROLanguageCode : NumericParameter = ...
        """
@index domain: language

@unit:
"""
        _PROLanguageCode : NumericParameter = ...
        """
"""
        PROAppCurrentDir : StringParameter = ...
        """
"""
        ClientDllIsPresent : NumericParameter = ...
        """
"""
        ConfigIdentifiers : Set = ...
        """
"""
        ModelName : StringParameter = ...
        """
"""
        ModelVersion : StringParameter = ...
        """
"""
        ModelDLLPath : StringParameter = ...
        """
"""
        HandleError : Procedure = ...
        """
"""
        Initialize : Procedure = ...
        """
All public declarations in this section should be available after calling pro::Initialize

"""
        GetListeningConnection : Procedure = ...
        """
"""
        CheckForNoEmpty : NumericParameter = ...
        """
"""
        RunLocally : Procedure = ...
        """
"""
        IsHandlingQueue : Procedure = ...
        """
"""
        GenerateDefaultLogConfigFile : Procedure = ...
        """
"""
        PROParseCommandlineArguments : Procedure = ...
        """
"""
        PROLoadClientConfiguration : Procedure = ...
        """
Read the parameters mandatory to the client, in the following order:
(1) Command-line arguments; (2) "pro_arguments.txt" in the project folder (when in development mode).

"""
        InternalListenConnectionID : StringParameter = ...
        """
"""
        ListenCallBack : Procedure = ...
        """
Callback that gets called right before handling every incoming message. Useful for debugging and logging purposes.

"""
        CreateListeningConnection : Procedure = ...
        """
"""
        CloseListeningConnection : Procedure = ...
        """
"""
        clientQueueID : StringParameter = ...
        """
"""
        workerQueueID : StringParameter = ...
        """
"""
        workerSessionID : StringParameter = ...
        """
"""
        workerDelegationLevel : NumericParameter = ...
        """
"""
        openedAsWorker : NumericParameter = ...
        """
"""
        workerCallbackCalled : NumericParameter = ...
        """
"""
        workerErrorMsg : StringParameter = ...
        """
Don't have the NoSave flag because it can be informed from worker to client.

"""
        workerRequestClientRef : StringParameter = ...
        """
"""
        workerRequestDescription : StringParameter = ...
        """
"""
        workerRequestProcedure : StringParameter = ...
        """
"""
        workerRequestTimeout : NumericParameter = ...
        """
"""
        workerInputDataVersion : StringParameter = ...
        """
"""
        workerOutputDataVersion : StringParameter = ...
        """
"""
        workerLogFileVersion : StringParameter = ...
        """
"""
        workerErrorMessage : StringParameter = ...
        """
"""
        workerActiveStatus : NumericParameter = ...
        """
"""
        workerErrorCode : NumericParameter = ...
        """
"""
        PublishingVerification : Procedure = ...
        """
"""
        PROWorkerHandleError : Procedure = ...
        """
"""
        PROWorkerInitialization : Procedure = ...
        """
"""
        PROWorkerFinalization : Procedure = ...
        """
"""
        PROWorkerListen : Procedure = ...
        """
"""
        PROWorkerRetrieveRequestInfo : Procedure = ...
        """
"""
        PROWorkerSaveRequestInfo : Procedure = ...
        """
"""
        SessionCompletedCallBackProxy : Procedure = ...
        """
"""
        RESTServiceHandlerPrototype : Procedure = ...
        """
"""
        AllLanguages : Set = ...
        """
This set should contain all languages for which you want to
localize your AIMMS end-user application. You can add new
languages at any time. However, you should always make sure
that your development language remains the first language
in the set. AIMMS will use this language to create new
localization entries during the automated localization
procedure as well as in the localization wizards.

"""
        LocalizedTextIndexSet : Set = ...
        """
This set is used to number all localized strings in your
end-user interface. The localization wizards automatically
update the definition of this set whenever new localization
strings are added. Therefore, you should not edit the
definition of this set by hand, unless you are sure
what you are doing.

"""
        LocalizedText : StringParameter = ...
        """
@index domain: (lti,language)

@unit:
This string parameter contains the actual localized strings
that are visible in the end-user interface. You can edit its
contents in the `Localized Text` window, which is accessible
through the `Tools-Localization` menu. The `Localized Text`
window is also opened when you invoke the `Data ...` menu
for any of the localization identifiers.

"""
        LocalizedTextDescription : StringParameter = ...
        """
@index domain: (lti)

@unit:
This string parameter contains an (optional) description for
each localization string. You can edit its contents in the
`Localized Text` window, which is accessible through the
`Tools-Localization` menu. The `Localized Text` window is
also opened when you invoke the `Data ...` menu for any of
the localization identifiers.

"""
        LocalizationReadLanguage : Procedure = ...
        """
This procedure reads the localization data for a single language.

"""
        LocalizationWriteLanguage : Procedure = ...
        """
This procedure writes the localization data for a single language.
AIMMS will only write data, if data for the language is actually
present. This will prevent loss of localization data which is
written without being read before.

"""
        LocalizationReadAll : Procedure = ...
        """
Execute this procedure if you intend to edit the localization
parameters by hand (i.e. without using the localization wizards).
In that case, do not forget to call LocalizationWriteAll before
the end of your AIMMS session.

"""
        LocalizationWriteAll : Procedure = ...
        """
You should execute this procedure if you have edited the
localization parameters by hand. Before editing, you can
call LocalizationReadAll to obtain all currently present
localization data.

"""
        LocalizationInitialize : Procedure = ...
        """
This procedure initializes localization support for your application.
It is automatically added to the end of MainInitialization during the
localization setup. If the element parameter CurrentLanguage already
has been assigned a value at that time, AIMMS will read the localization
strings for that language. In all other cases, the localization data
for the development language is read.

"""
        SetLogin : Procedure = ...
        """
"""
        GetOAuthCallbackData : Procedure = ...
        """
"""
        PROS_ROOT_USER_BUCKET : StringParameter = ...
        """
"""
        PROP_LIBPRJ_OK : NumericParameter = ...
        """
Key Code for Publishing: 0xA651

"""
        PROLastErrorMessage : StringParameter = ...
        """
"""
        PROSBufferSize : NumericParameter = ...
        """
"""
        PROLibraryInit : NumericParameter = ...
        """
"""
        PROCriticalError : NumericParameter = ...
        """
"""
        PROCancelLogin : NumericParameter = ...
        """
"""
        Finalize : Procedure = ...
        """
"""
        class session:
            sessionsToRemove : Set = ...
            """
"""
            warnString : StringParameter = ...
            """
"""
            ActiveSessionRunning : NumericParameter = ...
            """
"""
            LastKnownActiveSessionStatus : StringParameter = ...
            """
"""
            RetainSessionCases : NumericParameter = ...
            """
"""
            SaveSessionMessages : NumericParameter = ...
            """
"""
            ReconnectToRunningSessions : NumericParameter = ...
            """
"""
            ManagedSessions : Set = ...
            """
"""
            ManagedSessionsActive : Set = ...
            """
"""
            ManagedSessionsFinished : Set = ...
            """
"""
            BucketBasePath : StringParameter = ...
            """
"""
            MaxInitTimeout : NumericParameter = ...
            """
"""
            MaxCloseTimeout : NumericParameter = ...
            """
"""
            ClientQueueID : StringParameter = ...
            """
@index domain: manSess

@unit:
"""
            WorkerQueueID : StringParameter = ...
            """
@index domain: manSess

@unit:
"""
            LastKnownStatus : NumericParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            RequestTime : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            UserEnv : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            UserName : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            Application : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            OriginalCasePath : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            RequestDescription : StringParameter = ...
            """
@index domain: manSess

@unit:
"""
            RequestProcedure : StringParameter = ...
            """
@index domain: manSess

@unit:
"""
            RunTimeOut : NumericParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            VersionID : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            ResponseVersionID : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            MessageLogVersionID : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            ErrorMessage : StringParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            ActiveStatus : NumericParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            ErrorCode : NumericParameter = ...
            """
@index domain: (manSess)

@unit:
"""
            PostLoadInputCaseHook : ElementParameter = ...
            """
"""
            PostLoadResultCaseHook : ElementParameter = ...
            """
"""
            ServerErrorCallBackHook : ElementParameter = ...
            """
"""
            DefaultCallBack : Procedure = ...
            """
"""
            LoadResultsCallBack : Procedure = ...
            """
"""
            EmptyCallBack : Procedure = ...
            """
"""
            SessionCompletedCallBack : Procedure = ...
            """
"""
            ServerErrorCallBack : Procedure = ...
            """
"""
            LoadManagedSessions : Procedure = ...
            """
"""
            SetSessionData : Procedure = ...
            """
"""
            SetActiveSession : Procedure = ...
            """
"""
            RemoveManagedSession : Procedure = ...
            """
"""
            RunManagedSession : Procedure = ...
            """
"""
            OptimizeCurrentCase : Procedure = ...
            """
OBS: This procedure is supposed to be executed in the server side.

"""
            OptimizeCurrentCaseProxy : Procedure = ...
            """
OBS: This procedure is supposed to be executed in the server side.

"""
            OptimizeCurrentCaseInterrupted : Procedure = ...
            """
OBS: This procedure is supposed to be executed in the server side, when the user sends a
request to interrupt the current execution. As it has a "halt" effect in PRO execution,
this procedure set proper information about the session in the environment.

"""
            OptimizationCallBack : Procedure = ...
            """
"""
            OptimizationCallBackProxy : Procedure = ...
            """
"""
            InitializeUserProjectBuckets : Procedure = ...
            """
"""
            InitializeManagedSessions : Procedure = ...
            """
"""
            AuxEmpty : Procedure = ...
            """
Only to have a fixed dummy procedure to use as default

"""
        class version:
            DataManagementStyle : StringParameter = ...
            """
"""
            ManagedSessionInputCaseName : StringParameter = ...
            """
"""
            ManagedSessionOutputCaseName : StringParameter = ...
            """
"""
            ManagedSessionOutputCaseContainsDefinedIdentifiers : NumericParameter = ...
            """
    "If this parameter is 0, then the case file that is sent back from server to client does not include all the data
        of defined parameters and/or sets. This is the most efficient mode because the case file will be smaller and the client 
        will re-evaluate all defined identifiers anyway when reading in the case file.
        However, when you want to use the output cases from the server directly in a multiple case comparison, you should set
        this parameter to 1. Otherwise the data of these defined identifiers will show up as being empty."

"""
            SaveInputCase : Procedure = ...
            """
"""
            SaveOutputCase : Procedure = ...
            """
"""
            LoadCaseByFile : Procedure = ...
            """
"""
            LoadCaseAsCurrent : Procedure = ...
            """
"""
            GetCaseStatus : Procedure = ...
            """
"""
            ResetCaseStatus : Procedure = ...
            """
"""
            CaseFilePath : Procedure = ...
            """
"""
            FindCase : Procedure = ...
            """
"""
            NewCase : Procedure = ...
            """
"""
        ManagedSessionInputCaseIdentifierSet : Set = ...
        """
"""
        ManagedSessionOutputCaseIdentifierSet : Set = ...
        """
"""
        IsNewDataManagementStyle : NumericParameter = ...
        """
This is only there for backward compatibility (as it is part of the interface of AimmsProLibrary). 
It is now always 1

"""
        ManagedSessionRemoveFromCaseIdentifierSet : Set = ...
        """
The identifiers that are part of this set will always be removed when creating the input/output case. 
By default we do not want to store 'AllDefinedParameters' into the case we sent back and forth 
between a solver session in order to increase performance. Sometimes, e.g. when executing a case 
comparison, you do want to store definitions in the PRO input/output case. You can then assign the 
appropriate identifiers to remove (or just empty) to this value. For example AllDefinedParameters - 'MyParameter'.

"""
        DetermineDataManagementStyle : Procedure = ...
        """
No longer needed (always disk and folders now)

"""
        EP_DialogMessage : ElementParameter = ...
        """
"""
        EP_DialogAsk : ElementParameter = ...
        """
"""
        EP_StatusMessage : ElementParameter = ...
        """
"""
        DialogMessage : Procedure = ...
        """
"""
        DialogAsk : Procedure = ...
        """
"""
        StatusMessage : Procedure = ...
        """
"""
        class tdlg:
            DialogMessage : Procedure = ...
            """
"""
            DialogAsk : Procedure = ...
            """
"""
            StatusMessage : Procedure = ...
            """
"""
        class dlg:
            DialogMessage : Procedure = ...
            """
"""
            DialogAsk : Procedure = ...
            """
"""
            StatusMessage : Procedure = ...
            """
"""
        NativeUnicodeEncoding : ElementParameter = ...
        """
Because of a bug in earlier 3.14 versions, the specification of the default value is important here.

"""
        class management:
            IsRunningOnCloud : Procedure = ...
            """
Returns whether this session is running on the AIMMS cloud platform or not. 
When a Desktop session is launched from the AIMMS cloud platform it is considered to NOT be running on the AIMMS cloud platform.

"""
            RetrieveAccountInfo : Procedure = ...
            """
Returns a map (1 dimensional identifer infoValue with an index on the set infoKey) of key-value pairs representing some account characteristics. 
At the moment of writing there are values set for the keys DNS_NAME, CONCURRENT_SOLVES, CONCURRENT_USERS, CUSTOMIZATION_PROFILE and SOLVER_LICENSES.

"""
        class authentication:
            pass
        class sessionmanager:
            ListSessionsUsage : Procedure = ...
            """
"""
            FinishSession : Procedure = ...
            """
FinishSession is used to shutdow this session gracefully, e.g. to free up licenses or other resources.

"""
        class messaging:
            RuntimeErrors : StringParameter = ...
            """
"""
            GetQueueAuthorization : Procedure = ...
            """
"""
            UpdateQueueAuthorization : Procedure = ...
            """
"""
            WaitForMessages : Procedure = ...
            """
"""
            WaitForMessagesInternal : Procedure = ...
            """
"""
            GetMaxMessageQueueSize : Procedure = ...
            """
"""
            SetMaxMessageQueueSize : Procedure = ...
            """
Set the maximum message queue size; the default value is 3; values must be in the range (0, 100]

"""
            GetMaxMessagesPerSecond : Procedure = ...
            """
"""
            SetMaxMessagesPerSecond : Procedure = ...
            """
Set the maximum messages sent per second; the default value is 3; values must be in the range (0, 20]

"""
        class storage:
            ExistsBucket : Procedure = ...
            """
"""
            ExistsObject : Procedure = ...
            """
"""
        class publishing:
            pass
        class tunnel:
            TunnelStartWithLocalPort : Procedure = ...
            """
"""
            TunnelStartSSL : Procedure = ...
            """
"""
            TunnelStartGeneral : Procedure = ...
            """
"""
            TunnelStartGeneralWithLocalPort : Procedure = ...
            """
"""
        class client:
            pass
        class service:
            StartService : Procedure = ...
            """
"""
            LaunchService : Procedure = ...
            """
"""
            LaunchServiceJson : Procedure = ...
            """
"""
        class solverlease:
            AcquireSolverLease : Procedure = ...
            """
Attempts to acquire a lease for a solver license within the specified time for the specified duration. This procedure can be used to temporarily
upgrade a WebUI session that is running in the AIMMS cloud, to execute SOLVE statements (provided the solver lease is obtained) while potentially
blocking other solver sessions, depending on your cloud solver sessions capacity.

"""
            ReleaseSolverLease : Procedure = ...
            """
Releases the previous acquired lease on a solver license, see also AcquireSolverLease

"""
            GetLastSolverLeaseError : Procedure = ...
            """
Returns true when an error occured during lease-time of the solver and fills the lastError output parameter with an appropriate error message. 
Returns false otherwise

"""
            solveModel : Procedure = ...
            """
This procedure is wrapper around solver leases - it avoids leaking solver leases when there are errors during the solve. 
Limitation: this procedure only works in the AIMMS IDE and for AIMMS WebUI applications published on an AIMMS Cloud. 
            It specifically does not work for on premise deployments of PRO.
Note: The leaseMaxDuration is limited to 60 seconds, because otherwise solver lease is not applicable.

"""
        class authorization:
            pass
        BasicDataInitialization : Procedure = ...
        """
"""
        LibraryInitialization : Procedure = ...
        """
If opened in GUI mode, this procedure have restricted access to the model; so, it only checks for the DLL
and ask this same DLL to make an asynchronous call back to AIMMS to do the actual PRO initialization.
See procedure: LibraryInitializationGUI.

"""
        PostLibraryInitialization : Procedure = ...
        """
"""
        LibraryTermination : Procedure = ...
        """
"""
    class webui:
        TestStartServer : Procedure = ...
        """
"""
        ReadParameters : StringParameter = ...
        """
@index domain: CLI

@unit:
"""
        CommandLineArguments : Set = ...
        """
"""
        AIMMSIcons : Set = ...
        """
This set contain all the icons available in AIMMS that can be used in Widget Actions, Page Actions, Workflow steps and Status Bar messages.
The icons and their respective names are referenced here: https://documentation.aimms.com/_static/aimms-icons/icons-reference.html

"""
        ReturnStatuses : Set = ...
        """
"""
        ReturnStatusCode : NumericParameter = ...
        """
@index domain: rs

@unit:
"""
        IndexShowHideMode : Set = ...
        """
"""
        AllWebUIProperties : Set = ...
        """
"""
        OpenCloseStateProperty : Set = ...
        """
"""
        MessageLevels : Set = ...
        """
"""
        IsProjectDeveloperMode : NumericParameter = ...
        """
"""
        DataSessionId : StringParameter = ...
        """
"""
        DataSessionUser : StringParameter = ...
        """
"""
        DataSessionDNS : StringParameter = ...
        """
"""
        AimmsVersion : StringParameter = ...
        """
"""
        SessionType : StringParameter = ...
        """
"""
        AllPageIds : Set = ...
        """
This set contains the pageIds for pages of all types (see set AllPageTypes) that are created in WebUI.

"""
        AllPageTypes : Set = ...
        """
This set defines all the types of pages available in WebUI.

"""
        AllRegularPages : Set = ...
        """
A subset of AllPageIds that includes pageIds for Regular pages only.
Regular pages are pages that appear in the Navigation Menu and can also be used as part of Workflows.
These pageIds are used as an argument in the OpenPage procedure and to configure steps of a Workflow in the WorkflowPageSpecification set.

To identify which page is open in the WebUI, please check the data in webui::CurrentPageId which contains the pageIds for all open tabs.

"""
        AllSidePanelPages : Set = ...
        """
A subset of AllPageIds that includes pageIds for Side Panel pages.
These pageIds should be used to configure Side Panels in the SidePanelSpecification set.
Documentation: https://manual.aimms.com/webui/side-panels.html

To identify which sidepanel tab is open in the WebUI, please check the data in webui::CurrentSidePanelPageId which contains the pageIds for the sidepanel tab that is open in the WebUI.

"""
        AllDialogPages : Set = ...
        """
A subset of AllPageIds that includes pageIds for Dialog pages.
These pageIds are used as an argument in the OpenDialogPage procedure to invoke the respective Dialog page.
Documentation: https://manual.aimms.com/webui/dialog-pages.html

"""
        PageType : ElementParameter = ...
        """
@index domain: indexPageId

@unit:
An element parameter that maps each pageId (from the set AllPageIds) to its page type (from the set AllPageTypes).

"""
        PagePath : StringParameter = ...
        """
@index domain: indexPageId

@unit:
A string parameter that contains the path for each page created in the WebUI.

"""
        PageName : StringParameter = ...
        """
@index domain: indexPageId

@unit:
A string parameter that maps each pageId to the page name defined in the Page Manager in the WebUI.

"""
        SidePanelSpecification : Set = ...
        """
This set is used to configure Side Panels on pages. You will need to create string parameters indexed over this set.
The string parameters configured should be added in the respective page's Page Settings -> Page Extensions section.
Documentation: https://manual.aimms.com/webui/side-panels.html

"""
        WidgetActionSpecification : Set = ...
        """
This set is used to configure Widget Actions on widgets. You will need to create string parameters indexed over this set.

The string parameters configured should be added in the respective widget's Widget Settings -> Widget Actions section.

Widget Actions are available for the following widgets:
1. Table
2. Bar Chart
3. Line Chart
4. Pie Chart
5. Tree Map Chart
6. Gantt Chart
7. Bubble Chart
8. Map
9. Multiselect
10. Scalar (EXCEPT for the compact mode)
11. Legend
12. Slider
13. List

Documentation: https://manual.aimms.com/webui/widget-options.html#widget-actions

"""
        PageActionSpecification : Set = ...
        """
This set is used to configure the Primary Action and Secondary Actions on pages. You will need to create string parameters indexed over this set.
The string parameters configured should be added in the respective page's Page Settings -> Page Extensions section.
Documentation: https://manual.aimms.com/webui/page-settings.html#page-actions

"""
        WidgetItemActionSpecification : Set = ...
        """
This set is used to configure Item Actions in widgets. You will need to create string parameters indexed over this set.
The string parameters configured should be added in the respective widget's Widget Settings -> Widget Actions -> Item Actions option.

"""
        WorkflowPageSpecifications : Set = ...
        """
This set is used to configure the number of steps/pages in a specific Workflow. You will need to create a string parameter indexed over this set.
The string parameter configured should be added in the Application Settings -> Workflow Panel -> Workflow Steps field.
Documentation: https://manual.aimms.com/webui/application-settings.html#workflow-panel

"""
        WorkflowSpecifications : Set = ...
        """
This set is used to configure the number of Workflows in the application. You will need to create a string parameter indexed over this set.
The string parameter configured should be added in the Application Settings -> Workflow Panel -> Workflow field.
Documentation: https://manual.aimms.com/webui/application-settings.html#workflow-panel

"""
        ExtensionOrder : Set = ...
        """
A subset of the pre-declared set Integers, with several indices:
indexWorkflowOrder, used to reference the number of Workflows.
indexNoOfPages, used to reference the number of pages or steps in each Workflow.
indexPageExtension, used to reference the number of page extension such as Page Actions, Side Panels and Widget Actions.
indexApplicationExtension, used to reference the number of application extension such as Status Bar messages.
indexWidgetExtension, used to reference the number of widget extensions such as Widget Actions.
indexListOrder, used to reference the number of list groups.
indexNoOfListItems, used for defining number of list items per list group.

indexWorkflowOrder and indexNoOfPages are used as dimensions of the string parameters which will configure the Workflows and the steps of the Workflows in the application.
indexPageExtension is used as a dimension of the string parameter which will configure the Page Actions(Primary and Secondary), Side Panels and Widget Actions on pages and widgets respectively.
indexApplicationExtension is used as a dimension of the string parameter which will configure the Status Bar messages in the application.
indexWidgetExtension is used as a dimension of the string parameter which will configure the Widget Actions in a widget.
indexListOrder and indexNoOfListItems are used as dimensions of the string parameters which will configure the Lists and the List Items in the List widget.

The element parameters CurrentWorkflow and CurrentWorkflowStepdefined are used to identify the current Workflow and the current Workflow step respectively, that the user is on. (NOTE: This cannot be used currently, and the element parameters hold no values)

Documentation:
Workflows: https://manual.aimms.com/webui/application-settings.html#workflow-panel
Side Panels: https://manual.aimms.com/webui/page-manager.html#sidepanels
Page Actions: https://manual.aimms.com/webui/page-settings.html#page-actions
Widget Actions: https://manual.aimms.com/webui/widget-options.html#widget-actions
Status Bar: https://manual.aimms.com/webui/application-settings.html#status-bar
List Widget: https://manual.aimms.com/webui/list-widget.html

"""
        StatusBarSpecification : Set = ...
        """
This set is used to configure Status Messages on the Status Bar that appears on the footer. You will need to create string parameters indexed over this set.
The string parameters configured should be added in the Application Settings -> Application Extensions -> StatusBar Messages.
Documentation: https://manual.aimms.com/webui/status-bar.html

"""
        ListGroupSpecification : Set = ...
        """
This set is used to configure the number of group of lists to be displayed in the List widget. You will need to create a string parameter indexed over this set.
The string parameter configured should be added in the respective list widget's Widget Settings -> List settings -> List Groups.
Documentation: https://manual.aimms.com/webui/list-widget.html

"""
        ListGroupItemsSpecification : Set = ...
        """
This set is used to configure the list items in a specific list group. You will need to create a string parameter indexed over this set.
The string parameter configured should be added in the respective list widget's Widget Settings -> List settings -> List Items.
Documentation: https://manual.aimms.com/webui/list-widget.html

"""
        MenuBarSpecification : Set = ...
        """
This set is used to configure the Menu bar in the WebUI. To use it, create a string parameter indexed over this set.
The configured string parameter should then be added under Application Settings → Menu Bar Settings → Menu Bar.
For more details, refer to the documentation here https://documentation.aimms.com/webui/page-menu.html.

"""
        requestQueueMonitor : ElementParameter = ...
        """
"""
        Requests : Set = ...
        """
"""
        RequestQueueSize : NumericParameter = ...
        """
"""
        RequestCounter : NumericParameter = ...
        """
"""
        RequestQueue : StringParameter = ...
        """
@index domain: (rq,df)

@unit:
"""
        RequestPerformDialogInfo : StringParameter = ...
        """
@index domain: df

@unit:
"""
        DialogFields : Set = ...
        """
"""
        GetAllPages : Procedure = ...
        """
"""
        OpenSidePanel : Procedure = ...
        """
The procedure webui::OpenSidePanel opens a user-specified page as a side panel in the WebUI.
Arguments:
pageId: the pageId (from the AllSidePanelPages set) of the side panel page you want to open.

"""
        OpenPage : Procedure = ...
        """
The procedure webui::OpenPage opens a user-specified page in the WebUI
Arguments:
pageId: the pageId (from the set AllRegularPages) of the page you want to be opened.

"""
        OpenExternalLink : Procedure = ...
        """
The procedure webui::OpenExternalLink opens a user-specified URL on a new tab in the WebUI
Arguments:
url: the url of the external page you want to open.

"""
        ResetRequestQueue : Procedure = ...
        """
"""
        RequestPerformWebUIDialog : Procedure = ...
        """
The procedure webui::requestPerformWebUIDialog displays a message dialog in a WebUI page.
Along with the message we can also display buttons that are bound to custom actions.

Arguments:
title: A string parameter which contains the text to be displayed as the title of the dialog box.
message: A string parameter which contains the message to be displayed in the dialog box.
actions: A set of custom actions. The elements of this set are represented as buttons in the message dialog and their text is the same as the action names. When an action is selected (button is clicked), it invokes the onDone procedure with the corresponding action as an argument.
onDone: A reference to a procedure in the set AllProcedures. The procedure should have a single input string parameter as argument. When a user selects an action, the onDone procedure is invoked with the action name as its argument.

Remarks:
- When you just want to send a message to the user, you should provide a single action (e.g. Actions := {'OK'}) and you can use '' for the onDone argument. In this case, no procedure is called and the user can just close the 'dialog' by pressing the single action (or pressing the return/space key, which will press the default (last, highlighted) button).
- You can use a translation file (e.g. ‘WebUI/resources/languages/<dialog_actions>.properties’) to provide translations for the various internal action names, containing, for example: discard-and-continue = Discard and continue

"""
        OpenDialogPage : Procedure = ...
        """
The procedure webui::OpenDialogPage opens a user-specified page in a modal manner in the WebUI
Along with opening the page you can also display buttons that are bound to custom actions.

Arguments:
pageId: the pageId of the page you want to be opened as a modal dialog page.
title: A string parameter which contains the text to be displayed as the title of the dialog box.
actions: A set of custom actions. The elements of this set are represented as buttons in the message dialog and their text is the same as the action names. When an action is selected (button is clicked), it invokes the onDone procedure with the corresponding action as an argument.
onDone: A reference to a procedure in the set AllProcedures. The procedure should have a single input string parameter as argument. When a user selects an action, the onDone procedure is invoked with the action name as its argument.

"""
        IsWebUIDialogOpen : Procedure = ...
        """
The webui::IsWebUIDialogOpen procedure returns 1 if a dialog is open or displayed on WebUI, else it returns 0.

"""
        RequestFileUpload : Procedure = ...
        """
Use this method to initiate an upload in the (WebUI) browser (i.e. upload a file to the server/model)

"""
        RequestFileDownload : Procedure = ...
        """
Use this method to initiate a download in the (WebUI) browser (i.e. download a file from the server/model)

"""
        RequestShowNotification : Procedure = ...
        """
"""
        InitializeModelWebUIInteraction : Procedure = ...
        """
"""
        HandleCompletedRequests : Procedure = ...
        """
"""
        DetermineTimeZoneData : Procedure = ...
        """
"""
        InitializeTimeZoneData : Procedure = ...
        """
"""
        UponChange_DisplayTimeZone : Procedure = ...
        """
This procedure is invoked when the value of DisplayTimeZone changes when the Application Time Zone changes in the WebUI, which inturn invokes the procedure set in TimeZoneChangeHook.

"""
        UponChange_IgnoreDST : Procedure = ...
        """
This procedure is invoked when the value of IgnoreDST changes when the Consider daylight saving time switch changes in the WebUI, which inturn invokes the procedure set in TimeZoneChangeHook.

"""
        LocaleTimeZoneDisplayNameForBrowserTimeZone : StringParameter = ...
        """
This string parameter holds the value of the LocaleTimeZoneDisplayName that maps to the current user's browser time zone.

"""
        TimeZoneOffset : NumericParameter = ...
        """
@index domain: indexAllDisplayTimeZones

@unit:
"""
        DSTSettings : NumericParameter = ...
        """
@index domain: indexAllDisplayTimeZones

@unit:
This binary parameter is used to determine if a time zone has daylight saving time or not.

"""
        DefaultDSTSettingForDisplayTimeZone : NumericParameter = ...
        """
This binary parameter is used to determine if the daylight savings switch in the Time Zone Panel should be read-only for the selected webui::DisplayTimeZone.

"""
        BrowserTimeZoneMappingData : StringParameter = ...
        """
@index domain: (indexAllDisplayTimeZones in AllTimeZones,indexBrowser)

@unit:
This string parameter contains the mapping of time zones returned from different browsers and the time zones available in AIMMS.

"""
        BrowserTimeZoneMapping : StringParameter = ...
        """
@index domain: (indexAllDisplayTimeZones in AllTimeZones,indexBrowser)

@unit:
This string parameter contains the mapping of time zones returned from different browsers and the time zones available in AIMMS.

"""
        MappedBrowserTimeZone : ElementParameter = ...
        """
This element parameter holds the value of the AIMMS time zone that maps to the current user's browser time zone, from the webui::BrowserTimeZoneMapping identifier.

"""
        ActualLocaleTimeZoneDisplayName : StringParameter = ...
        """
@index domain: indexAllDisplayTimeZones

@unit:
"""
        AllDisplayTimeZones : Set = ...
        """
This set is used to define all the Time Zones that users can select in the WebUI, except Local and LocalDST which is used for AIMMS references.

"""
        DisplayTimeZones : Set = ...
        """
This set is used to display time zones with their respective offsets in the WebUI. eg: (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna.
Model developers can initialize this set with just specific time zones if required. When initializing, the time zones should be from the AllDisplayTimeZones set.

"""
        DisplayTimeZone : ElementParameter = ...
        """
An element parameter ranged over the DisplayTimeZones set, used to set the time zone for the application via the Time Zone Panel.

"""
        WebApplicationTimeZone : ElementParameter = ...
        """
This element parameter holds the value of the time zone that is set in the Application Time Zone (webui::DisplayTimeZone) in the Time Zone Panel. If webui::DisplayTimeZone is not initialized and is empty, ApplicationTimeZone is assigned the Local time zone where the application is hosted.
When configuring a calendar or string parameter that represents data and time, webui::WebApplicationTimeZone should be used in defining the Timeslot format and webui::DateTimeFormatIdentifier attributes respectively.

"""
        ModelTimeZone : ElementParameter = ...
        """
"""
        IgnoreDST : NumericParameter = ...
        """
A binary parameter that is used to toggle daylights saving time for the selected time zone in webui::DisplayTimeZone in the Time Zone Panel.

"""
        ApplicationHourlyTimeSlotFormat : StringParameter = ...
        """
This string parameter can be used in the Timeslot format in a calendar or webui::DateTimeFormatIdentifier in a string parameter to display the time format with or without "DST" based on the IgnoreDST setting, when the time is being displayed upto hours.

"""
        ApplicationMinuteTimeSlotFormat : StringParameter = ...
        """
This string parameter can be used in the Timeslot format in a calendar or webui::DateTimeFormatIdentifier in a string parameter to display the time format with or without "DST" based on the IgnoreDST setting, when the time is being displayed upto minutes.

"""
        TimeZoneChangeHook : ElementParameter = ...
        """
This element parameter is ranged over AllProcedures. As an application developer you can invoke any procedures when the value of webui::DisplayTimeZone or webui::IgnoreDST is changed in the WebUI.

"""
        ClientBrowsers : Set = ...
        """
This set includes a list of client browers and will be used to reference the Time Zone on the clients machine or the Local Time Zone.
The element parameter ClientBrowserName is used to initialize the users browser when the application is launched.

"""
        ClientBrowserName : ElementParameter = ...
        """
"""
        ClientBrowserLanguage : StringParameter = ...
        """
This string parameter is used to set the user's browser language when the application is launched.

"""
        BrowserTimeZone : StringParameter = ...
        """
This string parameter is used to set the user's browser time zone when the application is launched.

"""
        ApplicationConvention : ElementParameter = ...
        """
"""
        IDENTIFIER_SET : Index = ...
        """
@range: None
"""
        IdentifierVisibilities : Set = ...
        """
"""
        IndexVisibilities : Set = ...
        """
"""
        SetElementsAsJsonString : StringParameter = ...
        """
"""
        IdentifierElementText : StringParameter = ...
        """
@index domain: (IndexIdentifiers)

@unit:
"""
        IdentifierTooltip : StringParameter = ...
        """
@index domain: (IndexIdentifiers)

@unit:
"""
        IdentifierElementHtml : StringParameter = ...
        """
@index domain: (IndexIdentifiers)

@unit:
"""
        IdentifierHasBinaryRange : Procedure = ...
        """
"""
        NativeUnicodeEncoding : ElementParameter = ...
        """
Because of a bug in earlier 3.14 versions, the specification of the default value is important here.

"""
        CubeEngineLinkDLLPath : StringParameter = ...
        """
"""
        CubeEngineDLLPath : StringParameter = ...
        """
"""
        WebUILibraryPath : StringParameter = ...
        """
"""
        BuildVersion : StringParameter = ...
        """
"""
        GenerateAllPublicIdentifiersSet : Procedure = ...
        """
"""
        GetOrCreateImplicitPublicIdentifiers : Procedure = ...
        """
"""
        GetOrCreateExplicitPublicIdentifiers : Procedure = ...
        """
"""
        GetOrCreateDefaultPublicIdentifiers : Procedure = ...
        """
"""
        FindAllLibraryPrefixes : Procedure = ...
        """
"""
        AllAuthorizations : Set = ...
        """
"""
        AuthNone : ElementParameter = ...
        """
"""
        AuthR : ElementParameter = ...
        """
"""
        AuthRX : ElementParameter = ...
        """
"""
        AuthRW : ElementParameter = ...
        """
"""
        AuthRWX : ElementParameter = ...
        """
"""
        AllLibraryPrefixes : Set = ...
        """
"""
        IdentifierAuthorization : ElementParameter = ...
        """
@index domain: IndexIdentifiers

@unit:
"""
        LibraryAuthorization : ElementParameter = ...
        """
@index domain: (IndexLibraryPrefix)

@unit:
"""
        DefaultAuthorization : ElementParameter = ...
        """
"""
        Annotations : Set = ...
        """
"""
        AnnotationValues : StringParameter = ...
        """
@index domain: IndexIdentifiers

@unit:
"""
        AllAnnotationValues : StringParameter = ...
        """
@index domain: (a,IndexIdentifiers)

@unit:
"""
        InitializeAnnotations : Procedure = ...
        """
"""
        CheckForOldStyleAnnotations : Procedure = ...
        """
"""
        OptionEditorCategories : Set = ...
        """
"""
        LimitedOptionEditorCategory : NumericParameter = ...
        """
@index domain: indexOptionEditorCategories

@unit:
"""
        CurrentUserBelongsToGroup : Procedure = ...
        """
"""
        AllFormFieldNames : Set = ...
        """
"""
        FormDataChangeMonitorRef : ElementParameter = ...
        """
@index domain: rf

@unit:
"""
        MasterSelectionChangeMonitorRef : ElementParameter = ...
        """
@index domain: rf

@unit:
"""
        RegisteredForms : Set = ...
        """
"""
        HandleMasterSelectionChangedProcedureRef : ElementParameter = ...
        """
"""
        UpdateEntryCallbackProcedure : ElementParameter = ...
        """
@index domain: rf

@unit:
"""
        FormIsNewEntry : NumericParameter = ...
        """
@index domain: rf

@unit:
"""
        FormDialogHandlerOnDone : ElementParameter = ...
        """
"""
        FormDialogHandlerArg : StringParameter = ...
        """
"""
        SetupForm : Procedure = ...
        """

formId: the name/id of the form, must be a valid AIMMS identifier name
selInMaster: a one-dimensional parameter indexed over the same set that the detailsIndentifiers are indexed over
detailsIdentifiers: a set of parameters indexed over the same set as the selInMaster
validationHandler: a reference to a procedure(formData, validationErrors)
where:
                formData(webui::ffn)          - A string parameter containing all the raw form values, indexed over the detailsIdentifiers
                validationErrors(webui::ffn)  - A string parameter, to be updated by this validationHandler, that should contain all
                                                                                validation errors encountered in formData; also indexed over the detailsIdentifiers.
                                                                                Use webui::CreateValidationError("validation-error-some-error-id") to fill.
updateEntryCallback: a reference to a procedure(formData,selectedElementName)
where:
                formData(webui::ffn)          - A string parameter containing all the raw form values, indexed over the detailsIdentifiers
                selectedElementName           - The name of the element that this procedure should handle (i.e. create or update an element in the set
                                                                                which the selInMaster and the detailsIdentifiers are indexed over).

"""
        DefaultValidateFormProcedure : Procedure = ...
        """
"""
        AssertValidValidationError : Procedure = ...
        """
"""
        RequestPerformFormDialog : Procedure = ...
        """
"""
        CheckCubeEngineLinkDLLPathHasBeenInitialized : Procedure = ...
        """
"""
        CheckSetupFormArguments : Procedure = ...
        """
"""
        CreateCallValidateFormProcedure : Procedure = ...
        """
"""
        CreateUpdateFormWithNewSelectionProcedure : Procedure = ...
        """
"""
        CreateCopyFormToModeldentifiersProcedure : Procedure = ...
        """
"""
        CreateHandleMasterSelectionChangedProcedure : Procedure = ...
        """
"""
        CreateFormOperationsProcedures : Procedure = ...
        """
"""
        CreateHandleFormDataChangedProcedure : Procedure = ...
        """
"""
        DeleteRuntimeIdentifier : Procedure = ...
        """
"""
        HandleFormDialogResult : Procedure = ...
        """
"""
        DefaultUpdateEntryCallback : Procedure = ...
        """
"""
        GetFormSection : Procedure = ...
        """
"""
        GetOrCreateSharedFormSection : Procedure = ...
        """
"""
        SetupFormSection : Procedure = ...
        """
"""
        AddToAllImplicitPublicIdentifiers : Procedure = ...
        """
"""
        AssertValidFormId : Procedure = ...
        """
"""
        IsValidAnnotationId : Procedure = ...
        """
"""
        IsValidErrorId : Procedure = ...
        """
"""
        CreateHash : Procedure = ...
        """
"""
        NoOp1Form : Procedure = ...
        """
"""
        class proint:
            CaseFileSave : Procedure = ...
            """
"""
            FileExistsOnProStorage : Procedure = ...
            """
"""
            END_OF_STRING : NumericParameter = ...
            """
"""
            AccessFlags : Set = ...
            """
"""
            CheckFlag : Procedure = ...
            """
"""
            CreateCreatorFile : Procedure = ...
            """
"""
            ListObjectsWithEffectiveAuthorization : Procedure = ...
            """
"""
            HasReadAccess : Procedure = ...
            """
"""
            HasWriteAccess : Procedure = ...
            """
"""
        ActualCaseFileSave : ElementParameter = ...
        """
"""
        ActualCaseFileLoad : ElementParameter = ...
        """
"""
        ActualCaseFileURLtoElement : ElementParameter = ...
        """
"""
        DefaultCaseFileSave : Procedure = ...
        """
"""
        DefaultCaseFileLoad : Procedure = ...
        """
"""
        DefaultCaseFileURLtoElement : Procedure = ...
        """
"""
        CaseFileLoad : Procedure = ...
        """
"""
        ExistsWebUIStateHook : ElementParameter = ...
        """
Should return 0 if no state is present, 1 otherwise.
See Comment attribute of 'WebUI State Hook Declarations' section for more info.

"""
        RestoreWebUIStateHook : ElementParameter = ...
        """
See Comment attribute of 'WebUI State Hook Declarations' section for more info.

"""
        SaveWebUIStateHook : ElementParameter = ...
        """
See Comment attribute of 'WebUI State Hook Declarations' section for more info.

"""
        SaveAndReplaceActiveCase : Procedure = ...
        """
"""
        RefreshAllCasesEx : Procedure = ...
        """
"""
        LoadAndSetActiveCase : Procedure = ...
        """
"""
        SetActiveCase : Procedure = ...
        """
"""
        LoadCase : Procedure = ...
        """
"""
        SaveCase : Procedure = ...
        """
"""
        CreateCase : Procedure = ...
        """
"""
        DeleteCase : Procedure = ...
        """
"""
        AllWebUICases : Set = ...
        """
"""
        CasePath : StringParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        CaseReadOnly : NumericParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        CaseReadOnlyBool : StringParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        CompareCase : NumericParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        CompareCaseBool : StringParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        IsCaseModified : NumericParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        IsCaseModifiedBool : StringParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        IsCaseActiveBool : StringParameter = ...
        """
@index domain: (IndexWebUICases)

@unit:
"""
        ComparedCaseAnnotations : StringParameter = ...
        """
@index domain: IndexCurrentCaseSelection

@unit:
"""
        CurrentCasePath : StringParameter = ...
        """
"""
        CurrentCaseIsDirty : NumericParameter = ...
        """
"""
        CaseFileContentType : Set = ...
        """
"""
        ActiveCaseAnnotation : StringParameter = ...
        """
@index domain: IndexCurrentCaseSelection

@unit:
"""
        CaseReadOnlyAnnotation : StringParameter = ...
        """
@index domain: IndexCurrentCaseSelection

@unit:
"""
        LocalCaseDirectory : StringParameter = ...
        """
"""
        DetermineLocalCaseDirectory : Procedure = ...
        """
"""
        ExistsCase : Procedure = ...
        """
"""
        ExtendAllCasesFromPROStoragePath : Procedure = ...
        """
"""
        RefreshAllCases : Procedure = ...
        """
"""
        IsValidCase : Procedure = ...
        """
"""
        InitializeCurrentCase : Procedure = ...
        """
"""
        CompareCasePrevious : NumericParameter = ...
        """
@index domain: IndexWebUICases

@unit:
"""
        SyncCompareCaseToCurrentCaseSelection : Procedure = ...
        """
"""
        PostRunProcedureHook : Procedure = ...
        """
"""
        PostRequestSetValueHook : Procedure = ...
        """
"""
        LocalLogInfo : Procedure = ...
        """
"""
        Temp_CasePath : StringParameter = ...
        """
@index domain: IndexCases

@unit:
"""
        Temp_CaseReadOnlyBool : StringParameter = ...
        """
@index domain: IndexCases

@unit:
"""
        Temp_CompareCaseBool : StringParameter = ...
        """
@index domain: IndexCases

@unit:
"""
        Temp_CurrentCasePath : StringParameter = ...
        """
"""
        Temp_CurrentCaseIsDirty : NumericParameter = ...
        """
"""
        UseWebUIState : NumericParameter = ...
        """
"""
        SaveDataStateToTemp : Procedure = ...
        """
"""
        LoadDataStateFromTemp : Procedure = ...
        """
"""
        ExistsWebUIState : Procedure = ...
        """
"""
        DefaultExistsWebUIState : Procedure = ...
        """
"""
        RestoreWebUIState : Procedure = ...
        """
"""
        DefaultRestoreWebUIState : Procedure = ...
        """
"""
        SaveWebUIState : Procedure = ...
        """
"""
        DefaultSaveWebUIState : Procedure = ...
        """
"""
        QuitWebUI : Procedure = ...
        """
"""
        ResetAllDataChangeMonitors : Procedure = ...
        """
"""
        dataChangeMonitorRuntimeLibrary : ElementParameter = ...
        """
"""
        monitorIdCounter : NumericParameter = ...
        """
"""
        RegisteredDataChangeMonitors : Set = ...
        """
"""
        MonitoredDataChangedProcedures : ElementParameter = ...
        """
@index domain: rdcm

@unit:
"""
        ResetDataChangeMonitorProcedures : ElementParameter = ...
        """
@index domain: rdcm

@unit:
"""
        MonitoredIdentifierSets : ElementParameter = ...
        """
@index domain: rdcm

@unit:
"""
        RegisteredProcedures : ElementParameter = ...
        """
@index domain: rdcm

@unit:
"""
        tempGlobalMonitoredIdentifiers : Set = ...
        """
"""
        createDataChangeMonitorProcedures : Procedure = ...
        """
"""
        DataChangeMonitorRegisterCallback : Procedure = ...
        """
"""
        DataChangeMonitorUnregisterCallback : Procedure = ...
        """
"""
        DataChangeMonitorReset : Procedure = ...
        """
"""
        DataChangeMonitorsUpdate : Procedure = ...
        """
"""
        WebUIDLLPresent : Procedure = ...
        """
"""
        PROIsInitialized : Procedure = ...
        """
"""
        ParseCommandlineArguments : Procedure = ...
        """
"""
        LibraryInitialization : Procedure = ...
        """
"""
        LibraryTermination : Procedure = ...
        """
"""
        PreLibraryTermination : Procedure = ...
        """
"""
        PostLibraryInitialization : Procedure = ...
        """
"""
        MarkActiveTab : Procedure = ...
        """
This procedure is invoked when a tab marks that it is still active.

"""
        RemoveActiveTab : Procedure = ...
        """
This procedure is invoked when a tab marks that it is still active.

"""
        AllOpenWebUITabs : Set = ...
        """
This set contains all WebUI tabs currently open in the browser. Note: If a connection between the browser and the backend is lost, it may take a view moments for this tab to disappear from this list.

"""
        LastActiveWebUITab : ElementParameter = ...
        """
An element parameter ranged over the AllOpenWebUITabs set, used to indicate the last WebUI tab on which user interaction was recorded.

"""
        CurrentPageId : ElementParameter = ...
        """
@index domain: indexAllOpenWebUITabs

@unit:
This element parameter contains the PageIds of Regular page's for all open tabs in the WebUI.

"""
        CurrentSidePanelPageId : ElementParameter = ...
        """
@index domain: indexAllOpenWebUITabs

@unit:
This element parameter contains the SidePanel PageId for the currently opened sidepanel tab in the WebUI.

"""
        TabPingTimeStamp : NumericParameter = ...
        """
@index domain: indexAllOpenWebUITabs

@unit:s
"""
        TabUserInteractionTimeStamp : NumericParameter = ...
        """
@index domain: indexAllOpenWebUITabs

@unit:
"""
        CreateIdentifierIfNotPresent : Procedure = ...
        """
"""
        GetOrCreateWebUIRuntimeLibrary : Procedure = ...
        """
"""
        GetRuntimeIdentifierRef : Procedure = ...
        """
"""
        CreateRuntimeProcedure : Procedure = ...
        """
"""
        END_OF_STRING : NumericParameter = ...
        """
"""
        NoOp : Procedure = ...
        """
"""
        NoOp1 : Procedure = ...
        """
"""
        NoOp3 : Procedure = ...
        """
"""
        bAND : Procedure = ...
        """
returns the bitwise-AND: a & b

"""
        bOR : Procedure = ...
        """
returns the bitwise-OR: a | b

"""
        bit : Procedure = ...
        """
returns the n-th bit in a

"""
    class py:
        NativeUnicodeEncoding : ElementParameter = ...
        """
Because of a bug in earlier 3.14 versions, the specification of the default value is important here.

"""
        PythonChooserDLLPath : StringParameter = ...
        """
"""
        pyaimmsLibraryPath : StringParameter = ...
        """
"""
        DLLFolderPath : StringParameter = ...
        """
"""
        BuildVersion : StringParameter = ...
        """
"""
        python_version : StringParameter = ...
        """
"""
        current_dir : StringParameter = ...
        """
"""
        LibraryInitialization : Procedure = ...
        """
Add initialization statements here that do not require any other library being initialized already.

"""
        PostLibraryInitialization : Procedure = ...
        """
Add initialization statements here that require another library to be initialized already,
or add statements that require the Data Management module to be initialized.

"""
        PreLibraryTermination : Procedure = ...
        """
Add termination statements here that require all other libraries to be still alive.
Return 1 if you allow the termination sequence to continue.
Return 0 if you want to cancel the termination sequence.

"""
        LibraryTermination : Procedure = ...
        """
Add termination statements here that do not require other libraries to be still alive.
Return 1 to allow the termination sequence to continue.
Return 0 if you want to cancel the termination sequence.
It is recommended to only use the procedure PreLibraryTermination to cancel the termination sequence and let this procedure always return 1.

"""
    class webui_runtime:
        AllImplicitPublicIdentifiers : Set = ...
        """
"""
        AllDefaultPublicIdentifiers : Set = ...
        """
"""
        AllAllowedIdentifierTypes : Set = ...
        """
"""
        InitializeAllDefaultPublicIdentifiers : Procedure = ...
        """
"""
        AllExplicitPublicIdentifiers : Set = ...
        """
"""
        AllActualPublicIdentifiers : Set = ...
        """
"""
    class dcmr:
        DataChangeMonitor001_Set : Set = ...
        """
"""
        MonitoredDataChangedProcedure_for_DataChangeMonitor001_Set : Procedure = ...
        """
"""
        ResetDataChangeMonitor_for_DataChangeMonitor001_Set : Procedure = ...
        """
"""
    Carriers : Set = ...
    """
"""
    Orders : Set = ...
    """
"""
    Days : Set = ...
    """
"""
    Weeks : Set = ...
    """
"""
    SubOrders : Set = ...
    """
Orders assigned to the current (carrier, week) being routed in Phase 2

"""
    SubArcs : Set = ...
    """
Feasible arcs for current Phase 2 subproblem

"""
    OpenMarketCost : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    DedicatedFleetCost : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    Mileage : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    DueDay : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    WeekOf : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    LoadDays : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    LoadStart : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    EarliestStart : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    Feasible : NumericParameter = ...
    """
@index domain: (t, o)

@unit:
"""
    DeadheadMiles : NumericParameter = ...
    """
@index domain: (t, o)

@unit:
"""
    DistDestHome : NumericParameter = ...
    """
@index domain: (t, o)

@unit:
"""
    NDays : NumericParameter = ...
    """
"""
    P2_InterDH : NumericParameter = ...
    """
@index domain: (so, sop)

@unit:
Inter-order deadhead miles for current subproblem

"""
    P2_InterDHDays : NumericParameter = ...
    """
@index domain: (so, sop)

@unit:
Inter-order deadhead days for current subproblem

"""
    P2_ArcOK : NumericParameter = ...
    """
@index domain: (so, sop)

@unit:
1 iff arc so->sop is feasible in current subproblem

"""
    P2_CanEnd : NumericParameter = ...
    """
@index domain: so

@unit:
1 iff order so can end a tour (DistDestHome <= 100) for current carrier

"""
    P2_DHHome : NumericParameter = ...
    """
@index domain: so

@unit:
DeadheadMiles for current carrier to order origin

"""
    P2_DistHome : NumericParameter = ...
    """
@index domain: so

@unit:
DistDestHome for current carrier from order dest

"""
    P2_DHHomeDays : NumericParameter = ...
    """
@index domain: so

@unit:
travel_days(P2_DHHome)

"""
    P2_DistHomeDays : NumericParameter = ...
    """
@index domain: so

@unit:
travel_days(P2_DistHome)

"""
    P2_BigM : NumericParameter = ...
    """
Big-M for current subproblem

"""
    CurrentCarrier : ElementParameter = ...
    """
Element parameter pointing to the carrier being routed

"""
    CurrentWeek : NumericParameter = ...
    """
Week index being routed

"""
    Phase1Constraints : Set = ...
    """
"""
    Phase1Variables : Set = ...
    """
"""
    y : Variable = ...
    """
@index domain: (t, o) | Feasible(t, o)

@unit:
"""
    v : Variable = ...
    """
@index domain: o

@unit:
"""
    CostTW : Variable = ...
    """
@index domain: (t, w)

@unit:
"""
    total_cost : Variable = ...
    """
"""
    OrderFulfilled : Constraint = ...
    """
@index domain: o

@unit:
"""
    OneCarrier : Constraint = ...
    """
@index domain: o

@unit:
"""
    DailyCap : Constraint = ...
    """
@index domain: (t, d)

@unit:
"""
    DeadheadLimit : Constraint = ...
    """
@index domain: (t, w)

@unit:
"""
    CostFloorMinimum : Constraint = ...
    """
@index domain: (t, w)

@unit:
"""
    CostFloorEarned : Constraint = ...
    """
@index domain: (t, w)

@unit:
"""
    HomeDelivery : Constraint = ...
    """
@index domain: (t, o) | Feasible(t, o) and DistDestHome(t, o) > 100

@unit:
"""
    Phase2Constraints : Set = ...
    """
"""
    Phase2Variables : Set = ...
    """
"""
    p2_x : Variable = ...
    """
@index domain: (so, sop) | P2_ArcOK(so, sop)

@unit:
"""
    p2_zs : Variable = ...
    """
@index domain: so

@unit:
Tour starts from home at this order

"""
    p2_ze : Variable = ...
    """
@index domain: so

@unit:
Tour ends and returns home after this order

"""
    p2_s : Variable = ...
    """
@index domain: so

@unit:
Start day of loaded travel for this order

"""
    p2_obj : Variable = ...
    """
Minimize total deadhead for this carrier-week

"""
    P2_FlowIn : Constraint = ...
    """
@index domain: so

@unit:
"""
    P2_FlowOut : Constraint = ...
    """
@index domain: so

@unit:
"""
    P2_FixZEnd : Constraint = ...
    """
@index domain: so | not P2_CanEnd(so)

@unit:
"""
    P2_TimeSeq : Constraint = ...
    """
@index domain: (so, sop) | P2_ArcOK(so, sop)

@unit:
"""
    P2_SLower : Constraint = ...
    """
@index domain: so

@unit:
"""
    P2_DueDate : Constraint = ...
    """
@index domain: so

@unit:
"""
    P2_TourStart : Constraint = ...
    """
@index domain: so

@unit:
"""
    P2_TourEnd : Constraint = ...
    """
@index domain: so

@unit:
"""
    P2_DHLimit : Constraint = ...
    """
"""
    TourCarrier : ElementParameter = ...
    """
@index domain: o

@unit:
"""
    TourWeek : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    TourNumber : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    TourPosition : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    TourStartDay : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    TourDeadheadIn : NumericParameter = ...
    """
@index domain: o

@unit:
"""
    ReadInputData : Procedure = ...
    """
"""
    MainInitialization : Procedure = ...
    """
Add initialization statements here that do NOT require any library being initialized already.

"""
    Procedure_1 : Procedure = ...
    """
"""
    PostMainInitialization : Procedure = ...
    """
Add initialization statements here that require that the libraries are already initialized properly,
or add statements that require the Data Management module to be initialized.

"""
    MainExecution : Procedure = ...
    """
"""
    PreMainTermination : Procedure = ...
    """
"""
    MainTermination : Procedure = ...
    """
"""
