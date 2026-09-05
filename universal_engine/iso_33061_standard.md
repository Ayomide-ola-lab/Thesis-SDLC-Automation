PD ISO/IEC TS 33061:2021 











BSI Standards Publication 

**Information technology — Process assessment — Process assessment model for software life cycle processes** 



PD ISO/IEC TS 33061:2021 

PUBLISHED DOCUMENT 



### **National foreword** 

This Published Document is the UK implementation of ISO/IEC TS 33061:2021. It supersedes BS ISO/IEC 15504‑5:2012, which is withdrawn. 

The UK participation in its preparation was entrusted to Technical Committee IST/15, Software and systems engineering. 

A list of organizations represented on this committee can be obtained on request to its committee manager. 

###### **Contractual and legal considerations** 

This publication has been prepared in good faith, however no representation, warranty, assurance or undertaking (express or implied) is or will be made, and no responsibility or liability is or will be accepted by BSI in relation to the adequacy, accuracy, completeness or reasonableness of this publication. All and any such responsibility and liability is expressly disclaimed to the full extent permitted by the law. 

This publication is provided as is, and is to be used at the recipient’s own risk. 

The recipient is advised to consider seeking professional guidance with respect to its use of this publication. 

This publication is not intended to constitute a contract. Users are responsible for its correct application. 

This publication is not to be regarded as a British Standard. 

© The British Standards Institution 2021 Published by BSI Standards Limited 2021 

ISBN 978 0 539 15873 1 

ICS 35.080 

###### **Compliance with a Published Document cannot confer immunity from legal obligations.** 

This Published Document was published under the authority of the Standards Policy and Strategy Committee on 30 April 2021. 

###### **Amendments/corrigenda issued since publication** 

Date Text affected 

PD ISO/IEC TS 33061:2021 **ISO/TS 33061** 

TECHNICAL SPECIFICATION 



First edition 2021‑04‑20 

**Information technology — Process assessment — Process assessment model for software life cycle processes** 



Reference number ISO/TS 33061:2021(E) 

© ISO 2021 

PD ISO/IEC TS 33061:2021 **ISO/TS 33061:2021(E)** 





##### **COPYRIGHT PROTECTED DOCUMENT** 

©  ISO 2021, Published in Switzerland 

All rights reserved. Unless otherwise specified, no part of this publication may be reproduced or utilized otherwise in any form or by any means, electronic or mechanical, including photocopying, or posting on the internet or an intranet, without prior written permission. Permission can be requested from either ISO at the address below or ISO’s member body in the country of the requester. 

ISO copyright office Ch. de Blandonnet 8 • CP 401 CH‑1214 Vernier, Geneva, Switzerland Tel. +41 22 749 01 11 Fax +41 22 749 09 47 copyright@iso.org www.iso.org 

ii 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



### **Contents** 

###### Page 

|**Foreword**.....|........................|.............................................................................................................................................................................................................**v**|
|---|---|---|
|**Introductio**|**n**.....................|...........................................................................................................................................................................................................**vi**|
|**1**<br>**Scop**|**e**.....................|............................................................................................................................................................................................................**1**|
|**2**<br>**Norm**|**ative ref**|**erences**......................................................................................................................................................................................**1**|
|**3**<br>**Term**|**s and de**|**finitions**.....................................................................................................................................................................................**1**|
|**4**<br>**The**|**process a**|**ssessment model**.............................................................................................................................................................**1**|
|4.1|Genera<br>|l...........................................................................................................................................................................................................1<br>|
|4.2|Structu<br>|re of the process assessment model..................................................................................................................3<br>|
||4.2.1|General......................................................................................................................................................................................3|
||4.2.2|Processes................................................................................................................................................................................3|
||4.2.3|Process dimension.........................................................................................................................................................4|
||4.2.4|Quality dimension...........................................................................................................................................................4|
|4.3|Assess|ment indicators......................................................................................................................................................................4|
|**5**<br>**The**|**process d**|**imension**..................................................................................................................................................................................**5**|
|5.1|Genera|l...........................................................................................................................................................................................................5|
|5.2|Agreem|ent processes (AGR)........................................................................................................................................................6|
||5.2.1|General......................................................................................................................................................................................6|
||5.2.2|Acquisition process.......................................................................................................................................................6|
||5.2.3|Supply process...................................................................................................................................................................8|
|5.3|Organiz|ational project‑enabling processes (ORG)...................................................................................................9|
||5.3.1|General......................................................................................................................................................................................9|
||5.3.2<br>|Life cycle model management process.........................................................................................................9<br>|
||5.3.3<br>|Infrastructure management process...........................................................................................................10<br>|
||5.3.4|Portfolio management process.........................................................................................................................11|
||5.3.5|Human resource management process.....................................................................................................12|
||5.3.6|<br>Quality management process.............................................................................................................................13|
||5.3.7|Knowledge management process..................................................................................................................14|
|5.4|Technic|al management processes (MAN)....................................................................................................................15|
||5.4.1|General...................................................................................................................................................................................15|
||5.4.2|Project planning process........................................................................................................................................16|
||5.4.3|Project assessment and control process..................................................................................................17|
||5.4.4|Decision management process.........................................................................................................................19|
||5.4.5|Risk management process....................................................................................................................................20|
||5.4.6|Configuration management process............................................................................................................22|
||5.4.7|Information management process................................................................................................................24|
||5.4.8|Measurement process..............................................................................................................................................25|
||5.4.9|Quality assurance process....................................................................................................................................26|
|5.5|Technic|al processes (TEC).........................................................................................................................................................28|
||5.5.1|General...................................................................................................................................................................................28|
||5.5.2|Business or mission analysis process.........................................................................................................28|
||5.5.3|Stakeholder needs and requirements definition process..........................................................30|
||5.5.4|System/software requirements definition process........................................................................33|
||5.5.5|<br>Architecture definition process.......................................................................................................................35|
||5.5.6|Design definition process......................................................................................................................................38|
||5.5.7|<br>System analysis process..........................................................................................................................................40|
||5.5.8|<br>Implementation process........................................................................................................................................41|
||5.5.9|<br>Integration process.....................................................................................................................................................43|
||5.5.10|<br>Verification process....................................................................................................................................................45|
||5.5.11|Transition process.......................................................................................................................................................47|
||5.5.12|Validation process........................................................................................................................................................49|
||5.5.13|Operation process........................................................................................................................................................51|
||5.5.14|Maintenance process.................................................................................................................................................53|



iii 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|5.5.15 Disposal process............................................................................................................................................................55|
|---|
|**6**<br>**The quality dimension**.................................................................................................................................................................................**57**|
|**Annex A**(informative)**Process outputs**..........................................................................................................................................................**58**|
|**Bibliography**.............................................................................................................................................................................................................................**72**|



iv 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



### **Foreword** 

ISO (the International Organization for Standardization) is a worldwide federation of national standards bodies (ISO member bodies). The work of preparing International Standards is normally carried out through ISO technical committees. Each member body interested in a subject for which a technical committee has been established has the right to be represented on that committee. International organizations, governmental and non‑governmental, in liaison with ISO, also take part in the work. 

The procedures used to develop this document and those intended for its further maintenance are described in the ISO/IEC Directives, Part 1. In particular, the different approval criteria needed for the different types of ISO documents should be noted. This document was drafted in accordance with the editorial rules of the ISO/IEC Directives, Part 2 (see <u>www.iso.org/directives</u> or <u>www.iec. ch/members_experts/refdocs).</u> 

Attention is drawn to the possibility that some of the elements of this document may be the subject of patent rights. ISO shall not be held responsible for identifying any or all such patent rights. Details of any patent rights identified during the development of the document will be in the Introduction and/or on the ISO list of patent declarations received (see <u>www.iso.org/patents) or the IEClist of patent</u> declarations received (see http://patents.iec.ch). 

Any trade name used in this document is information given for the convenience of users and does not constitute an endorsement. 

For an explanation of the voluntary nature of standards, the meaning of ISO specific terms and expressions related to conformity assessment, as well as information about ISO's adherence to the World Trade Organization (WTO) principles in the Technical Barriers to Trade (TBT) see <u>www.iso. org/iso/foreword.html. In the IEC, see www.iec.ch/understanding‑standards.</u> 

This document was prepared by Joint Technical Committee ISO/IEC JTC 1, _Information technology,_ Subcommittee SC 7, _Software and systems engineering._ 

This document cancels and replaces <u>ISO/IEC 15504‑5:2012, which has been technically revised.</u> 

The main changes compared to <u>ISO/IEC 15504‑5:2012</u> are as follows: 

- all processes and their base practices are changed to reflect the ISO/IEC/IEEE 12207 processes; 

- all process related process outputs and their descriptions are revised; 

- this process assessment model includes a process quality attribute of process performance and can be used with other models of process quality, for instance capability as described in <u>ISO/IEC 33020.</u> 

Any feedback or questions on this document should be directed to the user’s national standards body. A complete listing of these bodies can be found at <u>www.iso.org/members.html</u> and <u>www.iec. ch/national‑committees.</u> 

© ISO 2021 – All rights reserved 

v 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



### **Introduction** 

The set of International Standards ISO/IEC 33001 to ISO/IEC 33099, termed the ISO/IEC 330xx family, defines the requirements and resources needed for process assessment. The overall architecture and content of the ISO/IEC 330xx family is described in ISO/IEC 33001. Several standards in the ISO/IEC 330xx family for process assessment are intended to replace and extend parts of the ISO/IEC 15504 series. Abstracts and previews of the ISO/IEC 330xx family of standards can be found on the ISO website. 

This document defines a process assessment model for software life cycle processes, conformant with the requirements of ISO/IEC 33004, for use in performing a conformant assessment in accordance with the requirements of <u>ISO/IEC 33002.</u> 

A process assessment model is related to one or more process reference models. The process reference model defined in ISO/IEC/IEEE 12207 is used as the basis for the process assessment model in this document. 

A process assessment model incorporates a process measurement framework conformant with the requirements of ISO/IEC 33003 and is expressed as a process quality characteristic with a defined set of process attributes. 

A process assessment model includes a set of assessment indicators. Process performance indicators address the process purpose and outcomes of each process in the process assessment model. Process quality indicators demonstrate the achievement of the process attributes in the process measurement framework. These indicators may also provide a reference source of practices when implementing a process improvement program. 

The assessment indicators are used as a basis for collecting objective evidence to support an assessor’s judgement in assigning ratings of the performance and quality of an implemented process. The set of indicators defined in this document are not intended to be an all-inclusive set and applicable in its entirety. Subsets appropriate to the context and scope of the assessment should be selected, and potentially augmented with additional indicators. 

A process assessment is conducted according to a documented assessment process. A documented assessment process identifies the rating method to be used in rating process attributes and identifies or defines the aggregation method to be used in determining ratings. 

<u>ISO/IEC 33020 provides a process measurement framework for the assessment of process</u> capability which may be incorporated as a process measurement framework in this document. ISO/IEC 33020:2019, Annex B includes a set of process quality indicators for each process attribute in the process measurement framework. 

vi 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 

**ISO/IEC TS 33061:2021** 

**TECHNICAL SPECIFICATION** 



## **Information technology — Process assessment — Process assessment model for software life cycle processes** 

#### **1 Scope** 

This document defines a process assessment model for software life cycle processes, conformant with the requirements of ISO/IEC 33004, for use in performing a conformant assessment in accordance with the requirements of <u>ISO/IEC 33002.</u> 

#### **2 Normative references** 

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies. 

ISO/IEC/IEEE 12207:2017, _Systems and software engineering — Software life cycle processes_ 

<u>ISO/IEC 33001,</u> _Information technology — Process assessment — Concepts and terminology_ 

<u>ISO/IEC 33003:2015,</u> _Information technology — Process assessment — Requirements for process measurement frameworks_ 

ISO/IEC 33004:2015, _Information technology — Process assessment — Requirements for process reference, process assessment and maturity models_ 

#### **3 Terms and definitions** 

For the purposes of this document, the terms and definitions given in <u>ISO/IEC 33001</u> apply. 

ISO and IEC maintain terminological databases for use in standardization at the following addresses: 

- ISO Online browsing platform: available at https://www.iso.org/obp 

- IEC Electropedia: available at <u>http://www.electropedia.org/</u> 

#### **4 The process assessment model** 

##### **4.1 General** 

This document provides a basis for a process assessment model that is two‑dimensional. In one dimension, the process dimension, the processes are defined and classified into process groups together with the set of assessment indicators of process performance. In the other dimension, the quality dimension, for each process attribute in the process measurement framework a set of process quality indicators is defined for the selected process quality characteristic. 

This document applies the software system concepts as defined in ISO/IEC/IEEE 12207. These concepts include software systems, software system architecture and enabling systems. 

NOTE 1 The software systems considered in this document are human‑made, created and utilized to provide products or services in defined environments for the benefit of users and other stakeholders. These software systems can include the following system elements: hardware, software, data, humans, processes (e.g. processes for providing service to users), procedures (e.g. operator instructions), facilities, services, materials and naturally occurring entities. As viewed by the user, they are thought of as products or services. (ISO/IEC/IEEE 12207) 

**1** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



NOTE 2 This document applies to systems for which software is of primary importance to the stakeholders. It is based upon the general principles of systems engineering and software engineering. It is a fundamental premise of this document that software always exists in the context of a system. Since software does not operate without hardware, the processor upon which the software is executed can be considered as part of the system. Alternatively, hardware or services hosting the software system and handling communications with other systems can also be viewed as enabling systems or external systems in the operating environment. The perception and definition of a particular software system, its architecture, and its elements depend on a stakeholder’s interests and responsibilities. One stakeholder’s system‑of‑interest can be viewed as a system element in another stakeholder’s system‑of‑interest. Furthermore, a system‑of‑interest can be viewed as being part of the environment for another stakeholder’s system‑of‑interest. (ISO/IEC/IEEE 12207) 

NOTE 3 The life cycle processes in this document are described in relation to a software system that is composed of interacting system elements (including software elements), each of which can be implemented to fulfil its respective specified requirements. Responsibility for the implementation of any system element may therefore be delegated to another party through an agreement. (ISO/IEC/IEEE 12207) 

NOTE 4 Throughout the life cycle of a system‑of‑interest, essential services are required from systems that are not directly a part of the operational environment of the system‑of‑interest, e.g. modelling system, training system, maintenance system. Each of these systems enables a part, e.g. a stage of the life cycle of the system‑ of‑interest to be conducted. Termed "enabling systems", they facilitate progression of the system‑of‑interest through its life cycle. (ISO/IEC/IEEE 12207) 



**Figure 1 — Structure of the process assessment model** 

<u>Figure 1</u> shows the process assessment model as a two‑dimensional model, the process dimension with its relationship to ISO/IEC/IEEE 12207 software life cycle processes, and the quality dimension in relationship to a process measurement framework. 

Users of this document may freely reproduce the detailed descriptions contained in the assessment model as part of any tool or other material to support the performance of process assessments, so that it can be used for its intended purpose. 

**2** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



##### **4.2 Structure of the process assessment model** 

###### **4.2.1 General** 

This subclause describes the detailed structure of the process assessment model and its key components. 

The process dimension comprises the set of processes defined with process purpose and process outcomes together with a set of assessment indicators of process performance. 

Processes included in a process reference model shall be in accordance with ISO/IEC 33004:2015, 5.4. 

The processes in this document are derived directly from ISO/IEC/IEEE 12207 and meet the ISO/IEC 33004 requirements for process descriptions, process purposes and outcomes. 

The quality dimension comprising a set of process attributes for a selected process quality characteristic is incorporated as a process measurement framework together with a set of process quality indicators. 

NOTE <u>ISO/IEC 33020 provides a process measurement framework for the assessment of process capability</u> which can be incorporated into this document. <u>ISO/IEC 33020 also includes a set of process quality indicators for</u> each process attribute in the process measurement framework. 

###### **4.2.2 Processes** 

The process assessment model is based upon the software life cycle processes defined in ISO/IEC/ IEEE 12207. The process reference model drawn from ISO/IEC/IEEE 12207 consists of the process purpose and outcomes defined in that standard. The purpose and outcomes are a statement of the goals of the performance of each process. 

In this document, ISO/IEC/IEEE 12207 serves as the process reference model for process assessments; any other use of the processes shall adhere to the requirements of ISO/IEC/IEEE 12207. 

<u>Figure 2 lists the processes from ISO/IEC/IEEE 12207 that are included in the process dimension of the</u> process assessment model and shows their classification into process groups. 

The process groups and their associated processes are described in Clause 5. The description of each process group includes a characterization of the processes it contains. In this process assessment model, each process belonging to a group is identified with a process identifier (ID) consisting of the group abbreviated name and the sequential number of the process in that group. 

**3** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 





**Figure 2 — Process groups** 

###### **4.2.3 Process dimension** 

Each process has a process identifier (ID) consisting of the process group abbreviated name and the sequential number of the process in that group. Each process is described by its name, purpose, outcomes, base practices, and process outputs. 

Each process is described in terms of a purpose statement. These statements contain the unique functional objectives of the process when performed in a particular environment. A list of specific process outcomes is associated with each of the process purpose statements, as a list of expected positive results of the process performance. 

###### **4.2.4 Quality dimension** 

For the quality dimension, the minimum requirement is that the process is performed, i.e. the implemented process achieves its process purpose and the expected outcomes are observable. 

Process attributes are features of a process that can be evaluated on a scale of achievement, providing a measure of the quality of the process and are applicable to all processes. 

##### **4.3 Assessment indicators** 

A process assessment model is based on the principle that the quality of a process can be assessed by demonstrating the achievement of process attributes on the basis of evidences related to assessment indicators. 

There are two types of assessment indicators: process performance indicators and process quality indicators. Process performance indicators address the process purpose and outcomes of each process in the process dimension. Process quality indicators demonstrate the achievement of the process attributes in the quality dimension. 

**4** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



The process performance indicators are: 

- base practice (BP); 

- process output (PO). 

The performance of base practices (BPs) provides an indication of the extent of achievement of the process purpose and process outcomes. The base practices correspond to ISO/IEC/IEEE 12207 activities and tasks. Process outputs (POs) are either used or produced (or both), when performing the process. Information items that are the key outputs of the process, are primarily used as performance indicators. 

<u>Annex A</u> provides the list of process outputs associated with the processes in <u>Clause 5. The process</u> outputs are identified by categories. The process outputs are indicated by the process IDs. 

Process quality indicators depend on the process quality characteristic of interest. The minimum requirement is that at least one of the process attributes shall comprise the achievement of the defined process purpose and process outcomes for the process; this is termed the process performance attribute (see ISO/IEC 33003:2015, 4.2.1). Other process quality attributes can be defined as needed. 

The process performance and process quality indicators represent types of objective evidence that can be found in an instantiation of a process and therefore can be used to judge achievement of quality. <u>Figure 3</u> shows how the assessment indicators are related to process performance and process quality. 







**Figure 3 — Assessment indicators** 

#### **5 The process dimension** 

##### **5.1 General** 

The process dimension comprises the set of processes defined with process purpose and process outcomes together with a set of assessment indicators of process performance. 

The individual processes each have a process identifier (ID) consisting of the process group abbreviated name and the sequential number of the process in that group and are described in terms of process 

**5** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



name, process purpose, and process outcomes as defined in ISO/IEC/IEEE 12207. The process group descriptions are compiled from ISO/IEC/IEEE 12207. 

In addition, the process dimension of the process assessment model provides information in the form of a set of: 

- a) base practices for the process providing a definition of the tasks and activities needed to accomplish the process purpose and fulfil the process outcomes; each base practice is associated to one or more process outcomes; 

b) process outputs that are related to one or more process outcomes; 

The process purposes, outcomes, base practices and process outputs associated with the processes are included in this clause. The base practices and process outputs constitute the set of indicators of process performance. 

A documented assessment process and assessor judgment is needed to ensure that process context (application domain, business purpose, development methodology, size of the organization, etc.) is explicitly considered when using this information. 

##### **5.2 Agreement processes (AGR)** 

###### **5.2.1 General** 

Organizations are producers and users of software systems. One organization (acting as an acquirer) can task another (acting as a supplier) for products or services. This is achieved using agreements. Agreements allow both acquirers and suppliers to realize value and support business strategies for their organizations. 

The agreement processes are organizational processes that apply outside of the span of a project’s life, as well as for a project’s lifespan. Generally, organizations act simultaneously or successively as both acquirers and suppliers of software systems. The agreement processes can be used with less formality when the acquirer and the supplier are in the same organization. Similarly, they can be used within the organization to agree on the respective responsibilities of organization, project and technical functions. 

This subclause specifies the requirements for the establishment of agreements with organizational entities external and internal to the organization. 

The agreement processes consist of the following: 

- a) acquisition process – used by organizations for acquiring products or services; 

- b) supply process – used by organizations for supplying products or services. 

These processes define the activities necessary to establish an agreement between two organizations. If the acquisition process is invoked, it provides the means for conducting business with a supplier. This may include products that are supplied for use as an operational software system, services in support of operational activities, software elements of a system, or elements of a software system being provided by a supplier. If the supply process is invoked, it provides the means for an agreement in which the result is a product or service that is provided to the acquirer. 

NOTE Security is an increasing concern in systems and software engineering. See ISO/IEC 27036 (all parts) for requirements and guidance for suppliers and acquirers on how to secure information in supplier relationships. Specific aspects of information security supplier relationships are addressed in <u>ISO/IEC 27036‑3:2013</u> and <u>ISO/IEC 27036‑4. (ISO/IEC/IEEE 12207)</u> 

###### **5.2.2 Acquisition process** 

**Process ID AGR.1 Process name Acquisition process** 

**6** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process purpose**|The purpose of the acquisition process is to obtain a product or service in ac‑<br>cordance with the acquirer's requirements.<br>NOTE As part of this process, the agreement is modified when a change request<br>is agreed to byboth the acquirer and supplier.|
|---|---|
|**Process outcomes**|As a result of the successful implementation of the acquisition process:<br>a) A request for supply is prepared.<br>b) One or more suppliers are selected.<br>c) An agreement is established between the acquirer and supplier.<br>d) A product or service complying with the agreement is accepted.<br>e)Acquirer obligations defined in the agreement are satisfied.|
|**Base practices **|**AGR.1.BP1: Prepare for the acquisition.**[Outcome: a]<br>1) Define a strategy for how the acquisition will be conducted.<br>2) Prepare a request for the supply of a product or service that includes the<br>requirements.<br>**AGR.1.BP2: Advertise the acquisition and select the supplier.**[Outcome: b]<br>1) Communicate the request for the supply of a product or service to potential<br>suppliers.<br>2) Select one or more suppliers.<br>**AGR.1.BP3: Establish and maintain an agreement.**[Outcome: c, d]<br>1) Develop an agreement with the supplier that includes acceptance criteria.<br>2) Identify necessary changes to the agreement.<br>3) Evaluate impact of changes on the agreement.<br>4) Negotiate the agreement with the supplier.<br>5) Update the agreement with the supplier, as necessary.<br>**AGR.1.BP4: Monitor the agreement.**[Outcome: d, e]<br>1) Assess the execution of the agreement.<br>2) Provide data needed by the supplier and resolve issues in a timely manner.<br>**AGR.1.BP5: Accept the product or service.**[Outcome: d, e]<br>1) Confirm that the delivered product or service complies with the agreement.<br>2) Provide payment or other agreed consideration.<br>3) Accept the product or service from the supplier, or other party, as directed<br>by the agreement.<br>4)Close the agreement.|
|**Process outputs**|Acquisition approach [Outcome: a]<br>Request for supply [Outcome: a]<br>Acquisition agreement [Outcome: c]<br>Acquisition agreement change request [Outcome: c]<br>Accepted system or system element (e.g. software) [Outcome: d]<br>Acquisition report [Outcome: e]<br>Acquisition record[Outcome: e]|



**7** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



###### **5.2.3 Supply process** 

|**Process ID **|**AGR.2**|
|---|---|
|**Process name **|**Supply process**|
|**Process purpose**|The purpose of the Supply process is to provide an acquirer with a product or<br>service that meets agreed requirements.|
|**Process outcomes**|As a result of the successful implementation of the Supply process:<br>a) An acquirer for a product or service is identified.<br>b) A response to the acquirer's request is produced.<br>c) An agreement is established between the acquirer and supplier.<br>d) A product or service is provided.<br>e) Supplier obligations defined in the agreement are satisfied.<br>f) Responsibility for the acquired product or service, as directed by the agree‑<br>ment, is transferred.|
|**Base practices **|**AGR.2.BP1: Prepare for the supply.**[Outcome: a]<br>1) Determine the existence and identity of an acquirer who has a need for a<br>product or service.<br>2) Define a supply strategy.<br>**AGR.2.BP2: Respond to a request for supply of products or services.**[Out‑<br>come: b]<br>1) Evaluate a request for the supply of a product or service to determine feasi‑<br>bility and how to respond.<br>2) Prepare a response that satisfies the solicitation.<br>**AGR.2.BP3: Establish and maintain an agreement.**[Outcome: c]<br>1) Negotiate an agreement with the acquirer that includes acceptance criteria.<br>2) Identify necessary changes to the agreement.<br>3) Evaluate impact of changes on the agreement.<br>4) Negotiate the agreement with the acquirer, as necessary.<br>5) Update the agreement with the acquirer, as necessary.<br>**AGR.2.BP4: Execute the agreement.**[Outcome: d, e]<br>1) Execute the agreement according to the established project plans.<br>2) Assess the execution of the agreement.<br>**AGR.2.BP5: Deliver and support the product or service.**[Outcome: d, e, f]<br>1) Deliver the product or service in accordance with the agreement criteria.<br>2) Provide assistance to the acquirer in support of the delivered product or ser‑<br>vice, per the agreement.<br>3) Accept and acknowledge payment or other agreed consideration.<br>4) Transfer the product or service to the acquirer, or other party, as directed by<br>the agreement.<br>5)Close the agreement.|



**8** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outputs**|Supply approach [Outcome: a]|
|---|---|
||Request for supply response [Outcome: b]|
||Supply agreement [Outcome: c]|
||Supply agreement change request [Outcome: c]|
||Supplied system [Outcome: d]|
||Supply report [Outcome: e, f]|
||Supplyrecord[Outcome: e, f]|



NOTE As part of this process, the agreement is modified when a change request affecting the terms of the agreement is agreed to by both the acquirer and supplier. (ISO/IEC/IEEE 12207) 

##### **5.3 Organizational project-enabling processes (ORG)** 

###### **5.3.1 General** 

The organizational project‑enabling processes are concerned with providing the resources to enable the project to meet the needs and expectations of the organization’s stakeholders. The organizational project‑enabling processes are typically concerned at a strategic level with the management and improvement of the organization’s business or undertaking, with the provision and deployment of resources and assets, and with its management of risks in competitive or uncertain situations. The organizational project‑enabling processes apply outside the span of a project’s life, as well as during a project’s lifespan. 

The organizational project‑enabling processes establish the environment in which projects are conducted. The organization establishes the processes and life cycle models to be used by projects; establishes, redirects, or cancels projects; provides resources required, including human and financial; and sets and monitors the quality measures for software systems and other deliverables that are developed by projects for internal and external customers. 

The organizational project‑enabling processes create a strong business image for many organizations and imply commercial and profit-making motives. Nevertheless, the organizational project-enabling processes are equally relevant to non-profit organizations, since they are also accountable to stakeholders, are responsible for resources, and encounter risk in their undertakings. This document can be applied to non-profit organizations as well as to profit-making organizations. 

The organizational project‑enabling processes help ensure the organization’s capability to acquire and supply products or services through the initiation, support and control of projects. These processes provide resources and infrastructure necessary to support projects and help ensure the satisfaction of organizational objectives and established agreements. They are not intended to be a comprehensive set of business processes that enable strategic management of the organization’s business. 

###### **5.3.2 Life cycle model management process** 

|**Process ID **|**ORG.1**|
|---|---|
|**Process name **|**Life cycle model managementprocess**|
|**Process purpose**|The purpose of the life cycle model management process is to define, maintain,<br>and assure availability of policies, life cycle processes, life cycle models, and pro‑<br>cedures for use by the organization with respect to the scope of this document.<br>This process provides life cycle policies, processes, models, and procedures that<br>are consistent with the organization's objectives, that are defined, adapted, im‑<br>proved and maintained to support individual project needs within the context<br>of the organization, and that are capable of being applied using effective, proven<br>methods and tools.|



**9** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the life cycle model management<br>process:<br>a) Organizational policies and procedures for the management and deployment<br>of life cycle models and processes are established.<br>b) Responsibility, accountability, and authority within life cycle policies, processes,<br>models, and procedures are defined.<br>c) Life cycle models and processes for use by the organization are assessed.<br>d)Prioritizedprocess, model, andprocedure improvements are implemented.|
|---|---|
|**Base practices **|**ORG.1.BP1: Establish the process.**[Outcome: a, b]<br>1) Establish policies and procedures for process management and deployment<br>that are consistent with organizational strategies.<br>2) Establish the processes that implement the requirements of this document<br>and that are consistent with organizational strategies.<br>3) Define the roles, responsibilities, accountabilities, and authorities to facilitate<br>implementation of processes and the strategic management of life cycles.<br>4) Define business criteria that control progression through the life cycle.<br>5) Establish standard life cycle models for the organization that are comprised<br>of stages, and define the purpose and outcomes for each stage.<br>**ORG.1.BP2: Assess the process.**[Outcome: c]<br>1) Monitor process execution across the organization.<br>2) Conduct periodic reviews of the life cycle models used by the projects.<br>3) Identify improvement opportunities from assessment results.<br>**ORG.1.BP3: Improve the process.**[Outcome: d]<br>1) Prioritize and plan improvement opportunities.<br>2)Implement improvement opportunities and inform relevant stakeholders.|
|**Process outputs**|Life cycle model management strategy [Outcome: a, c, d]<br>Organization policy [Outcome: a, b]<br>Organization procedure [Outcome: a, b]<br>Life cycle models [Outcome: a, b]<br>Organizational measurement needs [Outcome: c, d]<br>Organizational performance data [Outcome: c, d]<br>Life cycle model management report [Outcome: c, d]<br>Life cycle model management record[Outcome: c, d]|



###### **5.3.3 Infrastructure management process** 

|**Process ID **|**ORG.2**|
|---|---|
|**Process name **|**Infrastructure managementprocess**|
|**Process purpose**|The purpose of the infrastructure management process is to provide the infra‑<br>structure and services to projects to support organization and project objectives<br>throughout the life cycle.|
||This process defines, provides and maintains the facilities, tools, and communi‑<br>cations and information technology assets needed for the organization’s business<br>with respect to the scope of this document.|



**10** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the infrastructure management<br>process:<br>a) The requirements for infrastructure are defined.<br>b) The infrastructure elements are identified and specified.<br>c) Infrastructure elements are developed or acquired.<br>d)The infrastructure is available.|
|---|---|
|**Base practices **|**ORG.2.BP1: Establish the infrastructure.**[Outcome: a, b, c, d]<br>1) Define project infrastructure requirements.<br>2) Identify, obtain and provide infrastructure resources and services that are<br>needed to implement and support projects.<br>**ORG.2.BP2: Maintain the infrastructure.**[Outcome: a, b, c, d]<br>1) Evaluate the degree to which delivered infrastructure resources satisfy pro‑<br>ject needs.<br>2) Identify and provide improvements or changes to the infrastructure resources<br>as the project<br>requirements change.|
|**Process outputs**|Infrastructure management strategy [Outcome: b, c]<br>Infrastructure requirements [Outcome: a]<br>Organization infrastructure [Outcome: b, c, d]<br>Infrastructure change requests [Outcome: b, c]<br>Infrastructure management report [Outcome: d]<br>Infrastructure management record[Outcome: d]|



###### **5.3.4 Portfolio management process** 

|**Process ID **|**ORG.3**|
|---|---|
|**Process name **|**Portfolio managementprocess**|
|**Process purpose**|The purpose of the portfolio management process is to initiate and sustain nec‑<br>essary, sufficient and suitable projects in order to meet the strategic objectives<br>of the organization.<br>This process commits the investment of adequate organization funding and<br>resources, and sanctions the authorities needed to establish selected projects.<br>It performs continued assessment of projects to confirm they justify, or can be<br>redirected tojustify, continued investment.|
|**Process outcomes**|As a result of the successful implementation of the portfolio management process:<br>a) Business venture opportunities, investments or necessities are qualified and<br>prioritized.|
||b) Projects are identified.|
||c) Resources and budgets for each project are allocated.<br>d) Project management responsibilities, accountability, and authorities are defined.<br>e) Projects meeting agreement and stakeholder requirements are sustained.<br>f) Projects not meeting agreement or satisfying stakeholder requirements are<br>redirected or terminated.<br>g) Projects that have completed agreements and satisfied stakeholder require‑<br>ments are closed.|



**11** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**ORG.3.BP1: Define and authorize projects.**[Outcome: a, b, c, d]<br>1) Identify potential new or modified capabilities or missions.<br>2) Prioritize, select and establish new business opportunities, ventures or un‑<br>dertakings.<br>3) Define projects, accountabilities and authorities.<br>4) Identify the expected goals, objectives, and outcomes of each project.<br>5) Identify and allocate resources for the achievement of project goals and ob‑<br>jectives.<br>6) Identify multi‑project interfaces and dependencies to be managed or supported<br>by each project.<br>7) Specify the project reporting requirements and review milestones that govern<br>the execution of<br>each project.<br>8) Authorize each project to commence execution of project plans.<br>**ORG.3.BP2: Evaluate the portfolio of projects.**[Outcome: e, f]<br>1) Evaluate projects to confirm ongoing viability.<br>2) Act to continue or redirect projects that are satisfactorily progressing or can<br>be expected to progress satisfactorily by appropriate redirection.<br>**ORG.3.BP3: Terminate projects.**[Outcome: f, g]<br>1) Where agreements permit, act to cancel or suspend projects whose disadvan‑<br>tages or risks to the organization outweigh the benefits of continued investments.<br>2) After completion of the agreement for products and services, act to close the<br>projects.|
|---|---|
|**Process outputs**|Portfolio management strategy [Outcome: a, b, c, d, e, f, g]<br>Project portfolio [Outcome: a, b]<br>Project authorization [Outcome: c, d]<br>Project direction [Outcome: e, f, g]<br>Organization lessons learned [Outcome: e, f, g]<br>Portfolio management report [Outcome: e, f, g]<br>Portfolio management record[Outcome: e, f,g]|



NOTE For software systems, portfolio management also commonly refers to the management of a product line (portfolio of assets, products, and enabling systems, or service catalogue) to meet organizational or customer needs and objectives and support changes in technology. Management of assets is achieved through management of projects. (ISO/IEC/IEEE 12207) 

###### **5.3.5 Human resource management process** 

|**Process ID **|**ORG.4**|
|---|---|
|**Process name **|**Human resource managementprocess**|
|**Process purpose**|The purpose of the human resource management process is to provide the or‑<br>ganization with necessary human resources and to maintain their competencies,<br>consistent with business needs.<br>This process provides a supply of skilled and experienced personnel qualified<br>to perform life cycle processes to achieve organization, project, and stakeholder<br>objectives.|



**12** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the human resource management<br>process:<br>a) Skills required by projects are identified.<br>b) Necessary human resources are provided to projects.<br>c) Skills of personnel are developed, maintained or enhanced.<br>d)Conflicts in multi-project resource demands are resolved.|
|---|---|
|**Base practices **|**ORG.4.BP1: Identify skills.**[Outcome: a, c]<br>1) Identify skill needs based on current and expected projects.<br>2) Identify and record skills of personnel.<br>**ORG.4.BP2: Develop skills.**[Outcome: a, c]<br>1) Establish skills development strategy.<br>2) Obtain or develop training, education or mentoring resources.<br>3) Provide planned skill development.<br>4) Maintain records of skill development.<br>**ORG.4.BP3: Acquire and provide skills**. [Outcome: b, c, d]<br>1) Obtain qualified personnel when skill deficits are identified.<br>2) Maintain and manage the pool of skilled personnel necessary to staff ongoing<br>projects.<br>3) Make project assignments based on project and staff‑development needs.<br>4) Motivate personnel, e.g. through career development and reward mechanisms.<br>5)Control multi-project management interfaces to resolvepersonnel conflicts.|
|**Process outputs**|Human resource management strategy [Outcome: a, b, c, d]<br>Human resource requirements [Outcome: a]<br>Qualified personnel [Outcome: b, c, d]<br>Human resource management report [Outcome: c, d]|
||Human resource management record[Outcome: c, d]|



###### **5.3.6 Quality management process** 

|**Process ID **|**ORG.5**|
|---|---|
|**Process name **|**Quality managementprocess**|
|**Process purpose**|The purpose of the quality management process is to assure that products, services<br>and implementations of the quality management process meet organizational<br>andprojectqualityobjectives and achieve customer satisfaction.|
|**Process outcomes**|As a result of the successful implementation of the quality management process:<br>a) Organizational quality management policies, objectives, and procedures are<br>defined and implemented.|
||b) Quality evaluation criteria and methods are established.<br>c) Resources and information are provided to projects to support the operation<br>and monitoring of project quality assurance activities.<br>d) Quality assurance evaluation results are gathered and analysed.<br>e) Quality management policies and procedures are improved based upon project<br>and organizational results.|



**13** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**ORG.5.BP1: Plan quality management.**[Outcome: a, b, c]<br>1) Establish quality management policies, objectives, and procedures.<br>2) Define responsibilities and authority for implementation of quality management.<br>3) Define quality evaluation criteria and methods.<br>4) Provide resources and information for quality management.<br>**ORG.5.BP2: Evaluate quality management.**[Outcome: b, d]<br>1) Gather and analyse quality assurance evaluation results, in accordance with<br>the defined criteria.<br>2) Assess customer satisfaction.<br>3) Conduct periodic reviews of project quality assurance activities for compliance<br>with the quality management policies, objectives, and procedures.<br>4) Monitor the status of quality improvements on processes, products, and services.<br>**ORG.5.BP3: Perform corrective and preventive action.**[Outcome: d, e]<br>1) Plan corrective actions when quality management objectives are not achieved.<br>2) Plan preventive actions when there is a sufficient risk that quality management<br>objectives will not be achieved.<br>3) Monitor corrective and preventive actions to completion and inform relevant<br>stakeholders.|
|---|---|
|**Process outputs**|Quality management strategy [Outcome: a, b]<br>Quality management criteria and methods [Outcome: b]<br>Quality management system [Outcome: a, b, c, d, e]<br>Quality management corrective action [Outcome: c, e]<br>Quality management report [Outcome: d, e]<br>Quality management evaluation report [Outcome: d]<br>Qualitymanagement record[Outcome: d, e]|



NOTE Refer to <u>ISO 9001</u> for information and requirements to establish a quality management system. (ISO/IEC/IEEE 12207) 

###### **5.3.7 Knowledge management process** 

|**Process ID **|**ORG.6**|
|---|---|
|**Process name **|**Knowledge managementprocess**|
|**Process purpose**|The purpose of the knowledge management process is to create the capability<br>and assets that enable the organization to exploit opportunities to re‑apply<br>existing knowledge.<br>This encompasses knowledge, skills, and knowledge assets, including system<br>elements.|
|**Process outcomes**|As a result of the successful implementation of the knowledge management process:<br>a) A taxonomy for the application of knowledge assets is identified.<br>b) The organizational knowledge, skills, and knowledge assets are developed<br>or acquired.<br>c) The organizational knowledge, skills, and knowledge assets are available.<br>d)Knowledge management usage data isgathered and analysed.|



**14** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**ORG.6.BP1: Plan knowledge management.**[Outcome: a, b]|
|---|---|
||1) Define the knowledge management strategy.<br>2) Identify the knowledge, skills, and knowledge assets to be managed.<br>3) Identify projects that can benefit from the application of the knowledge, skills,<br>and knowledge assets.<br>**ORG.6.BP2: Share knowledge and skills throughout the organization.**[Out‑<br>come: b, c]<br>1) Establish and maintain a classification for capturing and sharing knowledge<br>and skills across the organization.<br>2) Capture or acquire knowledge and skills.<br>3) Share knowledge and skills across the organization.<br>**ORG.6.BP3: Share knowledge assets throughout the organization.**[Outcome:<br>b, c]<br>1) Establish a taxonomy to organize knowledge assets.<br>2) Develop or acquire knowledge assets.<br>3) Share knowledge assets across the organization.<br>**ORG.6.BP4: Manage knowledge, skills, and knowledge assets.**[Outcome: b, c, d]<br>1) Maintain knowledge, skills, and knowledge assets.<br>2) Monitor and record the reuse of knowledge, skills, and knowledge assets.<br>3) Periodically reassess the currency of technology and market needs for the<br>knowledge assets.|
|**Process outputs**|Knowledge management strategy [Outcome: a]<br>Knowledge management system [Outcome: b, c]<br>Knowledge asset [Outcome: b]<br>Knowledge management report[Outcome: d]|



NOTE The re‑application of existing knowledge is known as knowledge reuse and includes the reuse of knowledge about or from software elements. (ISO/IEC/IEEE 12207) 

##### **5.4 Technical management processes (MAN)** 

###### **5.4.1 General** 

The technical management processes are concerned with managing the resources and assets allocated by organization management and with applying them to fulfil the agreements into which the organization or organizations enter. The technical management processes relate to the technical effort of projects, in particular to planning in terms of cost, timescales and achievements, to the checking of actions to help ensure that they comply with plans and performance criteria and to the identification and selection of corrective actions that recover shortfalls in progress and achievement. These processes are used to establish and perform technical plans for the project, manage information across the technical team, assess technical progress against the plans for the software system, products, or services, control technical tasks through to completion, and aid in decision‑making. 

Typically, several projects co‑exist in one organization. The technical management processes can be employed at a corporate level to meet internal needs. 

The technical management processes are used to establish and evolve plans, to execute the plans, to assess actual achievement and progress against the plans, and to control execution through to fulfilment. Individual technical management processes may be invoked at any time in the life cycle 

**15** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



and at any level in a hierarchy of projects, as required by plans or unforeseen events. The technical management processes are applied with a level of rigor and formality that depends on the risk and complexity of the project. 

The scope of a technical management process is the technical management of a project or its products, to include the software product or system‑of‑interest. 

Project planning and project assessment and control processes are key to all management practices. These processes establish the general approach for managing a project or a process. The other processes in this group provide a specific focused set of tasks for achieving a specialized management objective. They are all evident in the management of any undertaking, ranging from a complete organization down to a single life cycle process and its tasks. In this document, the project has been chosen as the context for describing processes. The same processes can also be applied in the performance of services. 

###### **5.4.2 Project planning process** 

|**Process ID **|**MAN.1**|
|---|---|
|**Process name **|**Projectplanning process**|
|**Process purpose**|The purpose of the project planning process is to produce and coordinate effec‑<br>tive and workable plans.<br>This process determines the scope of the project management and technical<br>activities, identifies process outputs, tasks and deliverables, establishes sched‑<br>ules for task conduct, including achievement criteria, and required resources to<br>accomplish tasks. This is an on‑going process that continues throughout a project,<br>with regular revisions toplans.|
|**Process outcomes**|As a result of the successful implementation of the project planning process:<br>a) Objectives and plans are defined.<br>b) Roles, responsibilities, accountabilities, authorities are defined.<br>c) Resources and services necessary to achieve the objectives are formally re‑<br>quested and committed.<br>d)Plans for the execution of theproject are activated.|



**16** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**MAN.1.BP1: Define the project.**[Outcome: a, b]<br>1) Identify the project objectives and constraints.<br>2) Define the project scope as established in the agreement.<br>3) Define and maintain a life cycle model that is comprised of stages using the<br>defined life cycle models of the organization.<br>4) Establish a work breakdown structure (WBS) based on the deliverable prod‑<br>ucts or the evolving architecture of the software system.<br>5) Define and maintain the processes that will be applied on the project.<br>**MAN.1.BP2: Plan project and technical management.**[Outcome: b, c]<br>1) Define and maintain a project schedule based on management and technical<br>objectives and work estimates.<br>2) Define achievement criteria for the life cycle stage decision gates, delivery<br>dates and major dependencies on external inputs or outputs.<br>3) Define the costs and plan a budget.<br>4) Define roles, responsibilities, accountabilities, and authorities.<br>5) Define the infrastructure and services required.<br>6) Plan the acquisition of materials and enabling systems and services supplied<br>from outside the project.<br>7) Generate and communicate a plan for project and technical management and<br>execution, including reviews.<br>**MAN.1.BP3: Activate the project.**[Outcome: c, d]<br>1) Obtain approval for the project.<br>2) Submit requests and obtain commitments for necessary resources to perform<br>the project.|
|---|---|
||3)Implementprojectplans.|
|**Process outputs**|Project objectives [Outcome: a]<br>Project constraints [Outcome: a]<br>Project plan (e.g. software development plan) [Outcome: a]<br>Project budget [Outcome: b, c]<br>Work breakdown structure [Outcome: b, c]<br>Project schedule [Outcome: b, c]<br>Project infrastructure needs [Outcome: c]<br>Project human resources needs [Outcome: c]<br>Acquisition need [Outcome: c]|
||Projectplanningrecord[Outcome: d]|



NOTE The strategies defined in each of the other processes provide inputs and are integrated in the project planning process. The project assessment and control process is used to assess whether the plans are integrated, aligned, and feasible. (ISO/IEC/IEEE 12207) 

###### **5.4.3 Project assessment and control process** 

|**Process ID **|**MAN.2**|
|---|---|
|**Process name **|**Project assessment and controlprocess**|



**17** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process purpose**|The purpose of the project assessment and control process is to assess if the<br>plans are aligned and feasible; determine the status of the project, technical<br>and process performance; and direct execution to help ensure that the perfor‑<br>mance is according to plans and schedules, within projected budgets, to satisfy<br>technical objectives.<br>This process evaluates, periodically and at major events, the progress and achieve‑<br>ments against requirements, plans and overall business objectives. Information<br>is provided for management action when significant variances are detected. This<br>process also includes redirecting the project activities and tasks, as appropriate,<br>to correct identified deviations and variations from other technical management<br>or technicalprocesses. Redirection mayinclude re‑planningas appropriate.|
|---|---|
|**Process outcomes**|As a result of the successful implementation of the project assessment and con‑<br>trol process:<br>a) Performance measures or assessment results are available.|
||b) Adequacy of roles, responsibilities, accountabilities, and authorities is assessed.<br>c) Adequacy of resources is assessed.<br>d) Technical progress reviews are performed.<br>e) Deviations in project performance from plans are investigated and analysed.<br>f) Affected stakeholders are informed of project status.<br>g) Corrective action is defined and directed, when project achievement is not<br>meeting targets.<br>h) Project replanning is initiated, as necessary.<br>i) Project action to progress (or not) from one scheduled milestone or event to<br>the next is authorized.<br>j)Project objectives are achieved.|



**18** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**MAN.2.BP1: Plan for project assessment and control.**[Outcome: a]<br>1) Define the project assessment and control strategy.<br>**MAN.2.BP2: Assess the project.**[Outcome: b, c, d, e, f]<br>1) Assess alignment of project objectives and plans with the project context.<br>2) Assess management and technical plans against objectives to determine ad‑<br>equacy and feasibility.<br>3) Assess project and technical status against appropriate plans to determine<br>actual and projected cost, schedule, and performance variances.<br>4) Assess the adequacy of roles, responsibilities, accountabilities, and authorities.<br>5) Assess the adequacy and availability of resources.<br>6) Assess progress using measured achievement and milestone completion.<br>7) Conduct required management and technical reviews, audits and inspections.<br>8) Monitor critical processes and new technologies.<br>9) Analyse measurement results and make recommendations.<br>10) Record and provide status and findings from assessment tasks.<br>11) Monitor process execution within the project.<br>**MAN.2.BP3: Control the project.**[Outcome: g, h, i, j]<br>1) Initiate necessary actions needed to address identified issues.<br>2) Initiate necessary project replanning.<br>3) Initiate change actions when there is a contractual change to cost, time or<br>quality due to the impact of an acquirer or supplier request.<br>4)Authorize theproject toproceed toward the next milestone or event, ifjustified.|
|---|---|
|**Process outputs**|Project assessment and control approach [Outcome: a]<br>Project measurement needs [Outcome: a]<br>Project performance data [Outcome: a]<br>Project status report [Outcome: a, b, c, d, e, f]<br>Project review result [Outcome d]<br>Project control request [Outcome: g, h]<br>Project change request [Outcome: g, h]<br>Project authorization to proceed request [Outcome: i]<br>Project lessons learned [Outcome: j]<br>Project assessment and control record[Outcome:j]|



###### **5.4.4 Decision management process** 

|**Process ID **|**MAN.3**|
|---|---|
|**Process name **|**Decision managementprocess**|
|**Process purpose**|The purpose of the decision management process is to provide a structured,<br>analytical framework for objectively identifying, characterizing and evaluating<br>a set of alternatives for a decision at any point in the life cycle and select the most<br>beneficial course of action.|



**19** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the decision management process:|
|---|---|
||a) Decisions requiring alternative analysis are identified.<br>b) Alternative courses of action are identified and evaluated.<br>c) A preferred course of action is selected.<br>d)The resolution, decision rationale and assumptions are identified.|
|**Base practices **|**MAN.3.BP1: Prepare for decisions.**[Outcome: a]<br>1) Define a decision management strategy.<br>2) Identify the circumstances and need for a decision.<br>3) Involve relevant stakeholders in the decision‑making in order to draw on<br>experience and knowledge.|
||**MAN.3.BP2: Analyse the decision information.**[Outcome: b, d]<br>1) Select and declare the decision management strategy for each decision.<br>2) Determine desired outcomes and measurable selection criteria.<br>3) Identify the trade space and alternatives.<br>4) Evaluate each alternative, against the criteria.<br>**MAN.3.BP3: Make and manage decisions.**[Outcome: c, d]<br>1) Determine preferred alternative for each decision.<br>2) Record the resolution, decision rationale, and assumptions.<br>3)Record, track, evaluate and report decisions.|
|**Process outputs**|Decision management approach [Outcome: a]<br>Decision register [Outcome: a, c, d]<br>Decision management report [Outcome: b, c, d]<br>Decision management record[Outcome: d]|



NOTE 1 This process is used to resolve technical or project issues and respond to requests for decisions encountered during the software life cycle, in order to identify the alternative(s) that provides the preferred outcomes for the situation. The methods most frequently used for decision management are the trade study and engineering analysis. Each of the alternatives is assessed against the decision criteria (e.g. cost impact, schedule impact, programmatic constraints, regulatory implications, technical performance characteristics, critical quality characteristics, and risk). Results of these comparisons are ranked, via a suitable selection model, and are then used to decide on an optimal solution. Key study data (e.g. assumptions and decision rationale) are typically maintained to inform decision‑makers, and support future decision‑making. (ISO/IEC/IEEE 12207) 

NOTE 2 When it is necessary to perform a detailed assessment of a parameter for one of the criteria, the system analysis process is employed to perform the assessment. (ISO/IEC/IEEE 12207) 

###### **5.4.5 Risk management process** 

|**Process ID **|**MAN.4**|
|---|---|
|**Process name **|**Risk managementprocess**|
|**Process purpose**|The purpose of the risk management process is to identify, analyse, treat and<br>monitor the risks continually.<br>The risk management process is a continual process for systematically addressing<br>risk throughout the life cycle of a system product or service. It can be applied<br>to risks related to the acquisition, development, maintenance or operation of a<br>system.|



**20** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the risk management process:<br>a) Risks are identified.<br>b) Risks are analysed.<br>c) Risk treatment options are identified, prioritized, and selected.<br>d) Appropriate treatment is implemented.<br>e)Risks are evaluated to assess changes in status andprogress in treatment.|
|---|---|
|**Base practices **|**MAN.4.BP1: Plan risk management.**[Outcome: a, b, c]<br>1) Define the risk management strategy.<br>2) Define and record the context of the risk management process.<br>**MAN.4.BP2: Manage the risk profile.**[Outcome: a, b]<br>1) Define and record the risk thresholds and conditions under which a level of<br>risk may be accepted.<br>2) Establish and maintain a risk profile.<br>3) Periodically provide the relevant risk profile to stakeholders based upon their<br>needs.<br>**MAN.4.BP3: Analyse risks.**[Outcome: a, b, c, e]<br>1) Identify risks in the categories described in the risk management context.<br>2) Estimate the likelihood of occurrence and consequences of each identified risk.<br>3) Evaluate each risk against its risk thresholds.<br>4) For each risk that does not meet its risk threshold, define and record recom‑<br>mended treatment strategies and measures.<br>**MAN.4.BP4: Treat risks.**[Outcome: c, d, e]<br>1) Identify recommended alternatives for risk treatment.<br>2) Implement risk treatment alternatives for which the stakeholders determine<br>that actions should be taken to make a risk acceptable.<br>3) When the stakeholders accept a risk that does not meet its threshold, consider<br>it a high priority and monitor it continually to determine if future risk treatment<br>actions are necessary or if its priority has changed.<br>4) Once a risk treatment is selected, coordinate management action.<br>**MAN.4.BP5: Monitor risks.**[Outcome: a, c, e]<br>1) Continually monitor risks and the risk management context for changes and<br>evaluate the risks when their state has changed.<br>2) Implement and monitor measures to evaluate the effectiveness of risk treatments.<br>3) Continually monitor for the emergence of new risks and sources throughout<br>the life cycle.|
|**Process outputs**|Risk management approach [Outcome: a, b, c, d, e]<br>Risk register [Outcome: a, b, c, d, e]<br>Risk management report [Outcome: e]<br>Risk management record[Outcome: e]|



NOTE Risk is defined in ISO Guide 73 as "The effect of uncertainty on objectives". This has an attached Note 1, "An effect is a deviation from the expected — positive and/or negative." A positive risk is sometimes commonly known as an opportunity and addressed within the risk management process. (ISO/IEC/IEEE 12207) 

**21** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



###### **5.4.6 Configuration management process** 

|**Process ID **|**MAN.5**|
|---|---|
|**Process name **|**Configuration managementprocess**|
|**Process purpose**|The purpose of configuration management is to manage and control system el‑<br>ements and configurations over the life cycle. configuration management (CM)<br>also manages consistency between a product and its associated configuration<br>definition.|
|**Process outcomes**|As a result of the successful implementation of the configuration management<br>process:|
||a) Items requiring configuration management are identified and managed.<br>b) Configuration baselines are established.<br>c) Changes to items under configuration management are controlled.<br>d) Configuration status information is available.<br>e) Required configuration audits are completed.<br>f)System releases and deliveries are controlled and approved.|



**22** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**MAN.5.BP1: Plan configuration management.**[Outcome: a, b]<br>1) Define a configuration management strategy.<br>2) Define the storage, archive and retrieval procedures for configuration items,<br>CM artefacts, and records.<br>**MAN.5.BP2: Perform configuration identification.**[Outcome: a, b]<br>1) Select the software system elements to be uniquely identified as configuration<br>items subject to configuration control.<br>2) Identify the attributes of configuration items.<br>3) Define baselines through the life cycle.<br>4) Obtain acquirer and supplier agreement to establish a baseline.<br>**MAN.5.BP3:** **Perform configuration change management.**[Outcome: c, d, f]<br>1) Identify and record requests for change and requests for variance.<br>2) Coordinate, evaluate, and disposition requests for change and requests for<br>variance.<br>3) Track and manage approved changes to the baseline, requests for change and<br>requests for variance.<br>**MAN.5.BP4:** **Perform release control.**[Outcome: f]<br>1) Identify and record release requests, identifying the software system elements<br>in a release.<br>2) Approve software system releases and deliveries.<br>3) Track and manage distribution of software system releases to specified envi‑<br>ronments or software deliveries.<br>**MAN.5.BP5: Perform configuration status accounting.**[Outcome: d, e]<br>1) Develop and maintain the CM status information, for software system elements,<br>baselines, and releases.<br>2) Capture, store and report configuration management data.<br>**MAN.5.BP5: Perform configuration evaluation.**[Outcome: c, d, e,]<br>1) Identify the need for CM audits and schedule the events.<br>2) Verify the product configuration meets the configuration requirements by<br>comparing requirements, constraints, and waivers (variances) with results of<br>formal verification activities, which can involve sampling methods.<br>3) Monitor the incorporation of approved configuration changes.<br>4) Assess whether the software system meets the functional and performance<br>capabilities identified for the baseline.<br>5) Assess whether the operational software system elements conform to the<br>approved configuration information.<br>6)Record the CM audit results and disposition action items.|
|---|---|



**23** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outputs**|Configuration management approach [Outcome: a]<br>Configuration management system [Outcome: a, b, c, d, e, f]<br>Configuration baseline [Outcome: b]<br>Configuration management change request [Outcome c]<br>Configuration management variance request [Outcome c, f]|
|---|---|
||Configuration audit result [Outcome e]<br>Configuration management report [Outcome: a, b, c, d, e, f]|
||Configuration evaluation report [Outcome: d]<br>Configuration management record[Outcome: a, b, c, d, e, f]|



NOTE 1 Software configuration management (SCM) applies to both the software system and its interfaces. The purpose of interface management is to agree with interface partners on the exchange of data through communications among software systems and services. ISO/IEC/IEEE 12207:2017, E.5 provides an example of an interface management process view. (ISO/IEC/IEEE 12207) 

NOTE 2 Software configurations are changed through the controlled release of a new version. The purpose of a release is to authorize and effect the availability of a software feature, function, or system for a specific purpose, with or without restrictions to a subset of users. (ISO/IEC/IEEE 12207) 

###### **5.4.7 Information management process** 

|**Process ID **|**MAN.6**|
|---|---|
|**Process name **|**Information managementprocess**|
|**Process purpose**|The purpose of the information management process is to generate, obtain,<br>confirm, transform, retain, retrieve, disseminate and dispose of information, to<br>designated stakeholders.<br>Information management plans, executes, and controls the provision of information<br>to designated stakeholders that is unambiguous, complete, verifiable, consistent,<br>modifiable, traceable, and presentable. Information includes technical, project,<br>organizational, agreement and user information. Information is often derived<br>from data records of the organization, system,process, orproject.|
|**Process outcomes**|As a result of the successful implementation of the information management<br>process:<br>a) Information to be managed is identified.<br>b) Information representations are defined.<br>c) Information is obtained, developed, transformed, stored, validated, presented,<br>and disposed of.<br>d) The status of information is identified.<br>e)Information is available to designated stakeholders.|



**24** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**MAN.6.BP1: Prepare for information management.**[Outcome: a, b]<br>1) Define the strategy for information management.<br>2) Define the items of information that will be managed.<br>3) Designate authorities and responsibilities for information management.<br>4) Define the content, formats and structure of information items.<br>5) Define information maintenance actions.<br>**MAN.6.BP2: Perform information management.**[Outcome: c, d, e]<br>1) Obtain, develop, or transform the identified items of information.<br>2) Maintain information items and their storage records and record the status<br>of information.<br>3) Publish, distribute or provide access to information and information items to<br>designated stakeholders.<br>4) Archive designated information.<br>5)Dispose of unwanted, invalid or unvalidated information.|
|---|---|
|**Process outputs**|Information management approach [Outcome: a, b]<br>Information register [Outcome: a, b, c, d, e]<br>Information management report [Outcome: e]<br>Information management record[Outcome: c]|



NOTE Managed information has these quality characteristics: unambiguous, complete, verifiable, consistent, modifiable, traceable, and presentable. (ISO/IEC/IEEE 12207) 

###### **5.4.8 Measurement process** 

|**Process ID **|**MAN.7**|
|---|---|
|**Process name **|**Measurementprocess**|
|**Process purpose**|The purpose of the measurement process is to collect, analyse, and report ob‑<br>jective data and information to support effective management and demonstrate<br>thequalityof theproducts, services, andprocesses.|
|**Process outcomes**|As a result of the successful implementation of the measurement process:<br>a) Information needs are identified.<br>b) An appropriate set of measures, based on the information needs, is identified<br>or developed.|
||c) Required data is collected, verified, and stored.<br>d) The data is analysed and the results interpreted.<br>e)Information itemsprovide objective information that supports decisions.|



**25** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**MAN.7.BP1: Prepare for measurement.**[Outcome: a, b]<br>1) Define the measurement strategy.<br>2) Describe the characteristics of the organization that are relevant to measure‑<br>ment, such as business and technical objectives.<br>3) Identify and prioritize the information needs.<br>4) Select and specify measures that satisfy the information needs.<br>5) Define data collection, analysis, access, and reporting procedures.<br>6) Define criteria for evaluating the information items and the Measurement<br>process.<br>7) Identify and plan for the necessary enabling systems or services to be used.<br>**MAN.7.BP2: Perform measurement**. [Outcome: c, d, e]<br>1) Integrate manual or automated procedures for data generation, collection,<br>analysis and reporting into the relevant processes.<br>2) Collect, store, and verify data.<br>3) Analyse data and develop information items.<br>4)Record results and inform the measurement users.|
|---|---|
|**Process outputs**|Measurement approach [Outcome: a, b]<br>Measurement register [Outcome: a, b, c, d, e]<br>Measurement report [Outcome: d, e]<br>Measurement record[Outcome: c]|



NOTE Measures have these quality characteristics: verifiable, meaningful, actionable, timely, and costeffective. (ISO/IEC/IEEE 12207) 

###### **5.4.9 Quality assurance process** 

|**Process ID **|**MAN.8**|
|---|---|
|**Process name **|**Quality assuranceprocess**|
|**Process purpose**|The purpose of the quality assurance process is to help ensure the effective<br>application of the organization’s quality management process to the project.<br>Quality assurance (QA) focuses on providing confidence that quality requirements<br>will be fulfilled. Proactive analysis of the project life cycle processes and outputs<br>is performed to assure that the product being produced will be of the desired<br>qualityand that organization andprojectpolicies andprocedures are followed.|
|**Process outcomes**|As a result of the successful implementation of the quality assurance process:<br>a) Project quality assurance procedures are defined and implemented.<br>b) Criteria and methods for quality assurance evaluations are defined.<br>c)Evaluations of the project’s products, services, and processes are performed,<br>consistent with quality management policies, procedures, and requirements.<br>d) Results of evaluations are provided to relevant stakeholders.<br>e) Incidents are resolved.|
||f)Prioritizedproblems are treated.|



**26** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**MAN.8.BP1: Prepare for quality assurance.**[Outcome: a, b]<br>1) Define a quality assurance strategy.<br>2)Establish independence of quality assurance from other life cycle processes.<br>**MAN.8.BP2: Perform product or service evaluations.**[Outcome: b, c]<br>1)Evaluate products and services for conformance to established criteria, con‑<br>tracts, standards, and regulations.<br>2)Monitor that verification and validation of the outputs of the life cycle processes<br>are performed to determine conformance to specified requirements.<br>**MAN.8.BP3: Perform process evaluations.**[Outcome: c]<br>1)Evaluate project life cycle processes for conformance.<br>2)Evaluate tools and environments that support or automate the process for<br>conformance.<br>3)Evaluate supplier processes for conformance to process requirements.<br>**MAN.8.BP4: Manage QA records and reports.**[Outcome: d]<br>1)Create records and reports related to quality assurance activities.<br>2)Maintain, store, and distribute records and reports.<br>3)Identify incidents and problems associated with product, service, and process<br>evaluations.<br>**MAN.8.BP5: Treat incidents and problems.**[Outcome: d, e, f]<br>1) Record, analyse and classify incidents.<br>2) Identify selected incidents to associate with known errors or problems.<br>3) Record, analyse and classify problems.<br>4) Identify root causes and treatment of problems where feasible.<br>5) Prioritize treatment of problems (problem resolution) and track corrective<br>actions.<br>6) Analyse trends in incidents and problems.<br>7) Identify improvements in processes and products that may prevent future<br>incidents and problems.<br>8) Inform designated stakeholders of the status of incidents and problems.<br>9)Track incidents andproblems to closure.|
|---|---|
|**Process outputs**|Quality assurance approach [Outcome: a, b]<br>Quality assurance criteria and methods [Outcome: b]<br>Quality assurance system [Outcome: a, b, c, d, e]<br>Quality assurance corrective action [Outcome: e, f]<br>Quality assurance report [Outcome: d, e]<br>Quality assurance evaluation report [Outcome: c, d]<br>Qualityassurance record[Outcome: c, d, e, f]|



NOTE 1 Outcomes a) through d) align with the outcomes of the quality management process activities and tasks. (ISO/IEC/IEEE 12207) 

NOTE 2 IEEE 730‑2014 provides additional detail. (ISO/IEC/IEEE 12207) 

**27** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



##### **5.5 Technical processes (TEC)** 

###### **5.5.1 General** 

The technical processes are concerned with technical actions throughout the life cycle. Technical processes transform the needs of stakeholders into a product or service. By applying that product or operating that service, technical processes, provide sustainable performance, when and where needed in order to meet the stakeholder requirements and achieve customer satisfaction. The technical processes are applied in order to create and use a software system, whether it is in the form of a model or is an operational product. The technical processes apply at any level in a hierarchy of software system structure and at any stage in the life cycle. 

The technical processes are used to define the requirements for a software system, to transform the requirements into an effective product, to permit consistent reproduction of the product where necessary, to use the product to provide the required services, to sustain the provision of those services, and to dispose of the product when it is retired from service. 

The technical processes define the activities that enable organization and project functions to optimize the benefits and reduce the risks that arise from technical decisions and actions. These activities enable software systems and services to possess the timeliness and availability, cost effectiveness, functionality, reliability, maintainability, producibility, usability, and other qualities required by acquiring and supplying organizations. They also enable products and services to conform to the expectations or legislated requirements of society, including health, safety, security, and environmental factors. 

NOTE 1 For software systems, these processes can be recursively applied at more inclusive or more detailed levels for software system definition and realization. (ISO/IEC/IEEE 12207) 

NOTE 2 For software systems, these processes are often performed concurrently, iterating between one another to establish a solution that has satisfactory trade‑offs with respect to requirements, critical performance measures, and critical quality characteristics. At any level of abstraction, requirements and models are made consistent via iterations of applicable technical processes. When requirements and models are not directly capable of being implemented, the technical processes are applied recursively at a more detailed level or through different system views. (ISO/IEC/IEEE 12207) 

NOTE 3 The concept of life cycle stages and the application of these processes in any stage are described in detail in ISO/IEC/IEEE 24748‑1. It has a complete set of example stages and stage outcomes for the enactment of technical processes within a software life cycle. (ISO/IEC/IEEE 12207) 

NOTE 4 Interface management is a set of activities that cut across software engineering processes. These cross-cutting activities of the technical and technical management processes apply and track as a specific view of the processes and software system. See ISO/IEC/IEEE 12207:2017, E.5 for an example of an interface management process view. (ISO/IEC/IEEE 12207) 

NOTE 5 ISO/IEC 27002 and ISO/IEC 27034 provide guidance for applying security concerns in the technical processes for software systems. See ISO/IEC/IEEE 12207:2017, E.6 for a sample software assurance process view. (ISO/IEC/IEEE 12207) 

###### **5.5.2 Business or mission analysis process** 

|**Process ID **|**TEC.1**|
|---|---|
|**Process name **|**Business or mission analysisprocess**|
|**Process purpose**|The purpose of the business or mission analysis process is to define the business<br>or mission problem or opportunity, characterize the solution space, and deter‑<br>mine potential solution class(es) that can address a problem or take advantage<br>of an opportunity.|



**28** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the business or mission analysis<br>process:<br>a) The problem or opportunity space is defined.<br>b) The solution space is characterized.<br>c) Preliminary operational concepts and other concepts in the life cycle stages<br>are defined.<br>d) Candidate alternative solution classes are identified and analysed.<br>e) The preferred candidate alternative solution class(es) are selected.<br>f) Any enabling systems or services needed for business or mission analysis are<br>available.<br>g) Traceability of business or mission problems and opportunities and the pre‑<br>ferred alternative solution classes is established.|
|---|---|
|**Base practices **|**TEC.1.BP1: Prepare for business or mission analysis.**[Outcome: a, f]<br>1) Review identified problems and opportunities in the organization strategy<br>with respect to desired organization goals or objectives.<br>2) Define the business or mission analysis strategy.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support business or mission analysis.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.1.BP2: Define the problem or opportunity space.**[Outcome: b, c]<br>1) Analyse the problems and opportunities in the context of relevant trade‑space<br>factors.<br>2) Define the mission, business, or operational problem or opportunity.<br>**TEC.1.BP3: Characterize the solution space.**[Outcome: b, c, d]<br>1) Define preliminary operational concepts and other concepts in life cycle stages.<br>2) Identify candidate alternative solution classes that span the potential solution<br>space.<br>**TEC.1.BP4: Evaluate alternative solution classes.**[Outcome: d, e]<br>1) Assess each alternative solution class.<br>2) Select the preferred alternative solution class(es).<br>**TEC.1.BP5: Manage the business or mission analysis.**[Outcome: g]<br>1) Maintain traceability of business or mission analysis.<br>2)Provide keyartefacts and information items that have been selected for baselines.|



**29** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outputs**|Business or mission analysis approach [Outcome: a, b, c]<br>Problem or opportunity statement [Outcome: a]<br>Life cycle concepts [Outcome: c]|
|---|---|
||Validation criteria [Outcome: b]|
||Alternative solution classes [Outcome: b, d, e]|
||Requirements imposed on enabling systems [Outcome f]<br>Traceability mapping [Outcome: g]|
||Business or mission analysis record[Outcome: a, b, c, d, e, f,g]|



NOTE 1 Business and mission analysis is related to the organization encompassing stakeholders concerned by the activities of the software life cycle. This process interacts with the organization’s strategy, which is generally outside the scope of ISO/IEC/IEEE 12207. The results of the organization’s strategic analysis include the organizational concept of operations, strategic goals and plans, new market or mission elements, and identified problems and opportunities. The organization's strategy establishes the context within which the business or mission analysis is performed. The organizational concept of operations relates to the leadership’s intended way of operating the organization. It describes the organization’s assumptions and how it intends to use, acquire, or supply the system to be developed, existing systems, and possible future systems in support of an overall operation or series of operations of the business. In the case that the organization is the system‑of‑interest, the organization’s strategy is part of the system definition. (ISO/IEC/IEEE 12207) 

NOTE 2 This process has application through the life of the software system solution and can be revisited if there are changes in the environment, needs, or other drivers. (ISO/IEC/IEEE 12207) 

NOTE 3 In some domains, business or mission analysis relates to the concept of identifying and analysing capabilities that are needed or desired by the organization. This process focuses on the necessary capabilities and interacts with the portfolio management process for identifying the trade space that can address the capability. The identified problems or opportunities are often translated into target capabilities. As applicable within a given domain, the problem or opportunity space includes the target capabilities. (ISO/IEC/IEEE 12207) 

###### **5.5.3 Stakeholder needs and requirements definition process** 

|**Process ID **|**TEC.2**|
|---|---|
|**Process name **|**Stakeholder needs and requirements definitionprocess**|
|**Process purpose**|The purpose of the stakeholder needs and requirements definition process is to<br>define the stakeholder requirements for a system that can provide the capabilities<br>needed by users and other stakeholders in a defined environment.<br>It identifies stakeholders, or stakeholder classes, involved with the system<br>throughout its life cycle, and their needs. It analyses and transforms these needs<br>into a common set of stakeholder requirements that express the intended inter‑<br>action the system will have with its operational environment and that are the<br>reference against which each resulting operational capability is validated. The<br>stakeholder requirements are defined considering the context of the system of<br>interest with the interoperatingsystems and enablingsystems.|



**30** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the stakeholder needs and re‑<br>quirements Definition process:<br>a) Stakeholders of the system are identified.<br>b) Required characteristics and context of use of capabilities and concepts in the<br>life cycle stages, including operational concepts, are defined.<br>c) Constraints on a system are identified.<br>d) Stakeholder needs are defined.|
|---|---|
||e) Stakeholder needs are prioritized and transformed into clearly defined stake‑<br>holder requirements.|
||f) Critical performance measures are defined.|
||g) Stakeholder agreement that their needs and expectations are reflected ade‑<br>quately in the requirements is achieved.|
||h) Any enabling systems or services needed for stakeholder needs and require‑<br>ments are available.|
||i) Traceability of stakeholder requirements to stakeholders and their needs is<br>established.|



**31** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.2.BP1: Prepare for stakeholder needs and requirements definition.**<br>[Outcome: a, d, h]<br>1) Identify the stakeholders who have an interest in the software system through‑<br>out its life cycle.<br>2) Define the stakeholder needs and requirements definition strategy.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support stakeholder needs and requirements definition.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.2.BP2: Define stakeholder needs.**[Outcome: b, d, e]<br>1) Define context of use within the concept of operations and the preliminary<br>life cycle concepts.<br>2) Identify stakeholder needs.<br>3) Prioritize and down‑select needs.<br>4) Define the stakeholder needs and rationale.<br>**TEC.2.BP3: Develop the operational concept and other life cycle concepts.**<br>[Outcome: b, d]<br>1) Define a representative set of scenarios to identify required capabilities that<br>correspond to anticipated operational and other life cycle concepts.<br>2) Identify the factors affecting interactions between users and the system.<br>**TEC.2.BP4: Transform stakeholder needs into stakeholder requirements.**<br>[Outcome: c, d, e]<br>1) Identify the constraints on a system solution.<br>2)Identify the stakeholder requirements and functions that relate to critical<br>quality characteristics, such as assurance, safety, security, environment, or health.<br>3) Define stakeholder requirements, consistent with life cycle concepts, scenarios,<br>interactions, constraints, and critical quality characteristics.<br>**TEC.2.BP5: Analyse stakeholder requirements.**[Outcome: e, f, g]<br>1) Analyse the complete set of stakeholder requirements.<br>2) Define critical performance measures that enable the assessment of technical<br>achievement.<br>3) Feed back the analysed requirements to applicable stakeholders to validate<br>that their needs and expectations have been adequately captured and expressed.<br>4) Resolve stakeholder requirements issues.<br>**TEC.2.BP6: Manage the stakeholder needs and requirements definition.**<br>[Outcome: g, i]<br>1) Obtain explicit agreement with designated stakeholders on the stakeholder<br>requirements<br>2) Maintain traceability of stakeholder needs and requirements.<br>3)Provide keyartefacts and information items that have been selected for baselines.|
|---|---|



**32** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outputs**|Stakeholder needs and requirements definition approach [Outcome: a, b, c, d]<br>Stakeholder identification [Outcome: a]<br>Life cycle concepts [Outcome: b]<br>Stakeholder requirements [Outcome: e, g]<br>Validation criteria [Outcome: e, g]|
|---|---|
||Critical performance measurement needs [Outcome: f]|
||Critical performance data [Outcome: f]|
||Requirements imposed on enabling systems [Outcome h]<br>Traceability mapping [Outcome: i]|
||Stakeholder needs and requirements definition record [Outcome: a, b, c, d, e, f,<br>g, h, i]|



NOTE The SWEBOK, Guide to the Software Engineering Body of Knowledge, Software Requirements knowledge area discusses software requirements fundamentals (e.g. definition, types, properties, quality characteristics) and other topics, such as stakeholders, requirements elicitation, analysis, and management that provide additional guidance for software systems. (ISO/IEC/IEEE 12207) 

###### **5.5.4 System/software requirements definition process** 

|**Process ID **|**TEC.3**|
|---|---|
|**Process name **|**System/software requirements definitionprocess**|
|**Process purpose**|The purpose of the system/software requirements definition process is to trans‑<br>form the stakeholder, user‑oriented view of desired capabilities into a technical<br>view of a solution that meets the operational needs of the user.<br>This process creates a set of measurable system requirements that specify, from<br>the supplier’s perspective, what characteristics, attributes, and functional and<br>performance requirements the system is to possess, in order to satisfy stake‑<br>holder requirements. As far as constraints permit, the requirements should not<br>implyanyspecific implementation.|
|**Process outcomes**|As a result of the successful implementation of the system/software requirements<br>definition process:<br>a) The system or element description, including interfaces, functions and bound‑<br>aries, for a system solution is defined.<br>b) System/software requirements (functional, performance, process, non‑func‑<br>tional, and interface) and design constraints are defined.<br>c) Critical performance measures are defined.<br>d) The system/software requirements are analysed.<br>e) Any enabling systems or services needed for system/software requirements<br>definition are available.<br>f) Traceability of system/software requirements to stakeholder requirements<br>is developed.|



**33** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.3.BP1: Prepare for system/software requirements definition.**[Outcome:<br>a, b, e]<br>1) Define the functional boundary of the software system or element in terms of<br>the behaviour and properties provided.<br>2) Define the system/software requirements definition strategy.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support system/software requirements definition.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.3.BP2: Define system/software requirements.**[Outcome: b, d]<br>1) Define each function that the software system or element is required to perform.<br>2) Identify required states or modes of operation of the software system.<br>3) Define necessary implementation constraints.<br>4) Identify requirements that relate to risks, criticality of the software system,<br>or critical quality characteristics.<br>5) Define system/software requirements and requirements attributes.<br>**TEC.3.BP3: Analyse system/software requirements.**[Outcome: c, d]<br>1) Analyse the complete set of system/software requirements.<br>2) Define critical performance measures that enable the assessment of technical<br>achievement.<br>3) Feed back the analysed requirements to applicable stakeholders for review.<br>4) Identify and resolve issues, deficiencies, conflicts, and weaknesses within the<br>complete set of requirements.<br>**TEC.3.BP4: Manage system/software requirements.**[Outcome: d, f]<br>1) Obtain explicit agreement on the system/software requirements.<br>2) Maintain traceability of the system/software requirements.<br>3)Provide keyartefacts and information items that have been selected for baselines.|
|---|---|
|**Process outputs**|System/software requirements definition approach [Outcome: a, b, c]<br>System function model [Outcome: a]<br>System/software requirements [Outcome: a, b, d]<br>Verification criteria [Outcome: a, b, d]<br>Critical performance measurement needs [Outcome: c]<br>Critical performance data [Outcome: c]<br>Requirements imposed on enabling systems [Outcome e]<br>Traceability mapping [Outcome: f]<br>System/software requirements definition record[Outcome: a, b, c, d, e, f]|



NOTE 1 From a high-level view of the software system, this process can be used to define the overall requirements of the system. As the software system is decomposed into elements, each element, in turn, is treated as a system, function, or set of functions and this process can be used to further specify requirements. Requirements analyses and tools support traceability of requirements between the software system and its elements. (ISO/IEC/IEEE 12207) 

NOTE 2 The SWEBOK, Guide to the Software Engineering Body of Knowledge, Software Requirements knowledge area discusses software requirements definition, analysis, modelling, specification, validation, management and other topics that provide additional guidance for software systems. (ISO/IEC/IEEE 12207) 

**34** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



NOTE 3 The wording of the outcomes of the system/software requirements definition process differs slightly from the outcomes in the system requirements definition process of <u>ISO/IEC/IEEE 15288. Use of the</u> wording “system/software requirements” emphasize the applicability of this document to software systems, having software requirements and systems requirements. This is intended to assist users who define systems requirements and software requirements hierarchically or in different stages. (ISO/IEC/IEEE 12207) 

###### **5.5.5 Architecture definition process** 

|**Process ID **|**TEC.4**|
|---|---|
|**Process name **|**Architecture definitionprocess**|
|**Process purpose**|The purpose of the architecture definition process is to generate system archi‑<br>tecture alternatives, to select one or more alternative(s) that frame stakeholder<br>concerns and meet system requirements, and to express this in a set of consistent<br>views.<br>Iteration of the architecture definition process with the business or mission anal‑<br>ysis process, system requirements definition process, design definition process,<br>and stakeholder needs and requirements definition process is often employed<br>so that there is a negotiated understanding of the problem to be solved and a<br>satisfactory solution is identified. The results of the architecture definition pro‑<br>cess are widely used across the life cycle processes. Architecture definition may<br>be applied at many levels of abstraction, highlighting the relevant detail that is<br>necessaryfor the decisions at that level.|
|**Process outcomes**|As a result of the successful implementation of the architecture definition process:<br>a) Identified stakeholder concerns are addressed by the architecture.<br>b) Architecture viewpoints are developed.<br>c) Context, boundaries, and external interfaces of the system are defined.<br>d) Architecture views and models of the system are developed.<br>e) Concepts, properties, characteristics, behaviours, functions, or constraints<br>that are significant to architecture decisions of the system are allocated to ar‑<br>chitectural entities.<br>f) System elements and their interfaces are identified.<br>g) Architecture candidates are assessed.<br>h) An architectural basis for processes throughout the life cycle is achieved.<br>i) Alignment of the architecture with requirements and design characteristics<br>is achieved.<br>j) Any enabling systems or services needed for architecture definition are available.<br>k) Traceability of architecture elements to stakeholder and system/software<br>requirements is developed.|



**35** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices**|**TEC.4.BP1: Prepare for architecture definition.**[Outcome: a, b, c, h, j]|
|---|---|
|<br>|1) Review pertinent information and identify key drivers of the architecture.<br>2) Identify stakeholder concerns.<br>3) Define the architecture definition roadmap, approach, and strategy.<br>4) Define architecture evaluation criteria based on stakeholder concerns and<br>key requirements<br>5) Identify and plan for the necessary enabling systems or services needed to<br>support the architecture definition process.<br>6) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.4.BP2: Develop architecture viewpoints.**[Outcome: b, c, d, e]<br>1) Select, adapt, or develop viewpoints and model kinds based on stakeholder<br>concerns.<br>2) Establish or identify potential architecture framework(s) to be used in devel‑<br>oping models and views.<br>3) Capture rationale for selection of framework(s), viewpoints and model types.<br>4) Select or develop supporting modelling techniques and tools.<br>**TEC.4.BP3: Develop models and views of candidate architectures.**[Outcome:<br>b, c, d, e, f, h]<br>1) Define the software system context and boundaries in terms of interfaces and<br>interactions with external entities.<br>2) Identify architectural entities and relationships between entities that address<br>key stakeholder concerns and critical software system requirements.<br>3) Allocate concepts, properties, characteristics, behaviours, functions, or con‑<br>straints that are significant to architecture decisions of the software system to<br>architectural entities.<br>4) Select, adapt, or develop models of the candidate architectures of the software<br>system.<br>5) Compose views from the models in accordance with identified viewpoints to<br>express how the architecture addresses stakeholder concerns and meets stake‑<br>holder and system/software requirements.<br>6) Harmonize the architecture models and views with each other.<br>**TEC.4.BP4: Relate the architecture to design.**[Outcome: c, f, i, h]<br>1) Identify software system elements that relate to architectural entities and<br>the nature of these relationships.<br>2) Define the interfaces and interactions among the software system elements<br>and external entities.<br>3) Partition, align and allocate requirements to architectural entities and system<br>elements.<br>4) Map software system elements and architectural entities to design charac‑<br>teristics.<br>5)Defineprinciples for the software system design and evolution.|



**36** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|<br>|**TEC.4.BP5: Assess architecture candidates.**[Outcome: g, h, i]<br>1) Assess each candidate architecture against constraints and requirements.<br>2) Assess each candidate architecture against stakeholder concerns using eval‑<br>uation criteria.<br>3) Select the preferred architecture(s) and capture key decisions and rationale.<br>4) Establish the architecture baseline of the selected architecture.<br>**TEC.4.BP6: Manage the selected architecture.**[Outcome: h, i, k]<br>1) Formalize the architecture governance approach and specify governance<br>related roles and responsibilities, accountabilities, and authorities related to<br>design, quality, security, safety.<br>2) Obtain explicit acceptance of the architecture by stakeholders.<br>3) Maintain concordance and completeness of the architectural entities and their<br>architectural characteristics.<br>4) Organize, assess and control evolution of the architecture models and views<br>to help ensure that the architectural intent is met and the architectural vision<br>and key concepts are correctly implemented.<br>5) Maintain the architecture definition and evaluation strategy.<br>6) Maintain traceability of the architecture.<br>7)Provide keyartefacts and information items that have been selected for baselines.|
|---|---|
|**Process outputs**|Architecture definition approach [Outcome: a, h]<br>System/software architecture model [Outcome: b, c, d, e, f, g, h, i]<br>System/software architecture rationale [Outcome: b, c, d, e, f, g, h, i]<br>System/software interface definition [Outcome: c, f]<br>Critical performance measurement needs [Outcome: g]<br>Critical performance data [Outcome: g]<br>System/software architecture assessment report [Outcome: g]<br>Requirements imposed on enabling systems [Outcome j]<br>Traceability mapping [Outcome: k]<br>Architecture definition record[Outcome: h]|



NOTE 1 System architecture deals with fundamental principles, concepts, properties, and characteristics and their incorporation into the system-of-interest. Architecture definition has more uses than as merely a driver or part of design. Refer to ISO/IEC/IEEE 42010 for more information about architecture description and the uses and nature of architecture. (ISO/IEC/IEEE 12207) 

NOTE 2 The architecture definition process supports identification of stakeholders and their concerns. As the process unfolds, insights are gained into the relation between the requirements specified for the software system and the emergent properties and behaviours of the system that arise from the interactions and relations between the system elements. An effective architecture is as design‑agnostic as possible to allow for maximum flexibility in the design trade space. Even for a single-product software system, the design of the product will likely change over time while the architecture remains constant. An effective architecture also highlights and supports trade-offs for the design definition process and possibly other processes, such as portfolio management, project planning, system/software requirements definition, and verification. (ISO/IEC/IEEE 12207) 

NOTE 3 Architecture definition can apply to a product line rather than a single software system. A product line architecture describes the structural properties for building a group of related systems with common components and interrelationships. In product line architectures, the architecture necessarily spans several designs. The architecture serves to make the product line cohesive and helps ensure compatibility and interoperability across the product line. <u>ISO/IEC 26550</u> describes establishing a domain architecture for a product line. (ISO/IEC/IEEE 12207) 

**37** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



NOTE 4 The SWEBOK, Guide to the Software Engineering Body of Knowledge, Software Requirements, Software Design and Software Engineering Models and Methods knowledge areas discuss key aspects of software architecture in relationship to the system, as well as with respect to iteration with design. (ISO/IEC/IEEE 12207) 

###### **5.5.6 Design definition process** 

|**Process ID **<br>**Process name **|**TEC.5**<br> **Design definitionprocess**|
|---|---|
|**Process purpose**|The purpose of the design definition process is to provide sufficient detailed data<br>and information about the system and its elements to enable the implementa‑<br>tion consistent with architectural entities as defined in models and views of the<br>system architecture.|
|**Process outcomes**|As a result of the successful implementation of the design definition process:<br>a) Design characteristics of each system element are defined.<br>b) System/software requirements are allocated to system elements.<br>c) Design enablers necessary for design definition are selected or defined.<br>d) Interfaces between system elements composing the system are defined or<br>refined.<br>e) Design alternatives for system elements are assessed.<br>f) Design artefacts are developed.<br>g) Any enabling systems or services needed for design definition are available.<br>h) Traceability of the design characteristics to the architectural entities of the<br>system architecture is established.|
|**Base practices **<br>|**TEC.5.BP1: Prepare for software system design definition.**[Outcome: a, c, g]<br>1) Define the design definition strategy, consistent with the selected life cycle<br>model and anticipated design artefacts.<br>2) Select and prioritize design principles and design characteristics.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support design definition.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.5.BP2: Establish designs related to each software system element.**<br>[Outcome: b, c, d, e, f]<br>1) Transform architectural and design characteristics into the design of software<br>system elements.<br>2) Define and prepare or obtain the necessary design enablers.<br>3) Examine design alternatives and feasibility of implementation.<br>4) Refine or define the interfaces among the software system elements and with<br>external entities.<br>5) Establish the design artefacts.|



**38** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



###### **TEC.5.BP3 Assess alternatives for obtaining software system elements.** 

[Outcome: b, c, e, f] 1) Determine technologies required for each element composing the software system. 2) Identify candidate alternatives for the software system elements. 3) Assess each candidate alternative against criteria developed from expected design characteristics and element requirements to determine suitability for the intended application. 4) Choose the preferred alternatives among candidate design solutions for the software system elements. **TEC.5.BP4 Manage the design.** [Outcome: a, b, h] 1) Capture the design and rationale. 2) Establish traceability between the detailed design elements, the system/ software requirements, and the architectural entities of the software system architecture. 3) Determine the status of the software system and element design. 4) Provide key artefacts and information items that have been selected for baselines. **<mark>Process outputs</mark>** Design definition approach [Outcome: a, b, c] System/software design model [Outcome: a, c, d, f] System/software design rationale [Outcome: a, c, d, f] System/software interface definition [Outcome: d] System element (e.g. software) description [Outcome: a, b, d, e, f] Critical performance measurement needs [Outcome: e] Critical performance data [Outcome: e] System design assessment report [Outcome: e] Requirements imposed on enabling systems [Outcome g] Traceability mapping [Outcome: h] Design definition record [Outcome: f] 

NOTE 1 For software systems, design activities typically iterate with activities in system/software requirements definition and architecture definition. Design definition is typically applied iteratively and incrementally to develop a detailed design, including software elements, interfaces, databases, and user documentation. Software design is usually concurrent with software implementation, integration, verification, and validation. ISO/IEC/IEEE 12207:2017, Annex H discusses software design using agile methods. During design and implementation, further process application refines allocation of evolving requirements among software elements. (ISO/IEC/IEEE 12207) 

NOTE 2 The design definition process is driven by requirements that have been vetted through the architecture and more detailed analyses of feasibility. Architecture focuses on suitability, viability, and desirability, whereas design focuses on compatibility with technologies and other design elements and feasibility of implementation and integration. An effective architecture is as design-agnostic as possible to allow for maximum flexibility in the design trade space. (ISO/IEC/IEEE 12207) 

NOTE 3 This process provides feedback to the software system architecture to consolidate or confirm the allocation, partitioning and alignment of architectural entities. (ISO/IEC/IEEE 12207) 

**39** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



NOTE 4 Design definition considers applicable technologies and their contribution to the system solution. Design provides the ‘implement-to’ level of the definition, such as drawings, state diagrams, stories, and detailed design descriptions. For software elements, this process can result in a detailed design description that can be verified against requirements and the software architecture. Even if the software design is not fully specified in a formal description, it is sufficiently detailed to permit software implementation (construction) and test planning. (ISO/IEC/IEEE 12207) 

NOTE 5 The SWEBOK, Guide to the Software Engineering Body of Knowledge, provides detailed discussion on software design. This knowledge area addresses fundamentals, key issues, design strategies and methods, and design notations. (ISO/IEC/IEEE 12207) 

###### **5.5.7 System analysis process** 

|**Process ID **|**TEC.6**|
|---|---|
|**Process name **|**System analysisprocess**|
|**Process purpose**|The purpose of the system analysis process is to provide a rigorous basis of data<br>and information for technical understanding to aid decision‑making across the<br>life cycle.<br>The system analysis process applies to the development of inputs needed for<br>any technical assessment. It can provide confidence in the utility and integrity<br>of system requirements, architecture, and design. System analysis covers a wide<br>range of differing analytic functions, levels of complexity, and levels of rigor. It<br>includes mathematical analysis, modelling, simulation, experimentation, and<br>other techniques to analyse technical performance, system behaviour, feasibility,<br>affordability, critical quality characteristics, technical risks, life cycle costs, and<br>to perform sensitivity analysis of the potential range of values for parameters<br>across all life cycle stages. It is used for a wide range of analytical needs con‑<br>cerning operational concepts, determination of requirement values, resolution<br>of requirements conflicts, assessment of alternative architectures or system<br>elements, and evaluation of engineering strategies (integration, verification,<br>validation, and maintenance). Formality and rigor of the analysis will depend on<br>the criticality of the information need or work product supported, the amount of<br>information/data available, the size of theproject, and the schedule for the results.|
|**Process outcomes**|As a result of the successful implementation of the system analysis process:<br>a) System analyses needed are identified.<br>b) System analysis assumptions and results are validated.<br>c) System analysis results are provided for decisions.<br>d) Any enabling systems or services needed for system analysis are available.<br>e)Traceabilityof the system analysis results is established.|



**40** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.6.BP1: Define the system analysis strategy and prepare for system**<br>**analysis.**[Outcome: a, c, d]<br>1) Identify the problem or question that requires analysis.<br>2) Identify the stakeholders of the analysis.<br>3) Define the scope, objectives, and level of fidelity of the analysis.<br>4) Select the methods to support the analysis.<br>5) Identify and plan for the necessary enabling systems or services needed to<br>support the analysis.<br>6) Obtain or acquire access to the enabling systems or services to be used.<br>7) Collect the data and inputs needed for the analysis.<br>**TEC.6.BP2: Perform system analysis.**[Outcome: b, c]<br>1) Identify and validate contexts and assumptions.<br>2) Apply the selected analysis methods to perform the required analysis.<br>3) Review the analysis results for quality and validity.<br>4) Establish conclusions and recommendations.<br>5) Record the results of the system analysis.<br>**TEC.6.BP3: Manage the system analysis.**[Outcome: e]<br>1) Maintain traceability of the analysis results.<br>2)Provide keyartefacts and information items that have been selected for baselines.|
|---|---|
|**Process outputs**|System analysis approach [Outcome a, b]<br>Requirements imposed on enabling systems [Outcome d]<br>Traceability mapping [Outcome: e]<br>System analysis report [Outcome c]<br>System analysis record[Outcome c, e]|



NOTE The system analysis process can be employed for the entire software system or any element. This process is often used in conjunction with the decision management process. (ISO/IEC/IEEE 12207) 

###### **5.5.8 Implementation process** 

|**Process ID **|**TEC.7**|
|---|---|
|**Process name **|**Implementationprocess**|
|**Process purpose**|The purpose of the implementation process is to realize a specified system element.<br>This process transforms requirements, architecture, design, including interface,<br>into actions that create a system element according to the practices of the selected<br>implementation technology, using appropriate technical specialties or disciplines.<br>This process results in a system element that satisfies specified system require‑<br>ments(includingallocated and derived requirements), architecture, and design.|



**41** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the implementation process:<br>a) Implementation constraints that influence the requirements, architecture, or<br>design are identified.<br>b) A system element is realized.<br>c) A system element is packaged or stored.<br>d) Any enabling systems or services needed for implementation are available.<br>e)Traceabilityis established.|
|---|---|
|**Base practices **|**TEC.7.BP1: Prepare for implementation.**[Outcome: a, d]<br>1) Define an implementation strategy.<br>2) Identify constraints from the implementation strategy and implementation<br>technology on the system/software requirements, architecture characteristics,<br>design characteristics, or implementation techniques.<br>3) Identify and plan for the necessary and distinct software environments, in‑<br>cluding enabling systems or services needed to support implementation.<br>4) Obtain or acquire access to the software environments and other enabling<br>systems or services.<br>**TEC.7.BP2: Perform implementation.**[Outcome: b, c]<br>1) Realize or adapt software elements, according to the strategy, constraints,<br>and defined implementation procedures.<br>2) Realize or adapt hardware elements of software systems.<br>3) Realize or adapt service elements of software systems.<br>4) Evaluate software unit and affiliated data or other information according to<br>the implementation strategy and criteria.<br>5) Package and store the software system element.<br>6) Record objective evidence that the software system element meets requirements.<br>**TEC.7.BP3: Manage results of implementation.**[Outcome: e]<br>1) Record implementation results and anomalies encountered.<br>2) Maintain traceability of the implemented software system elements.<br>3)Provide keyartefacts and information items that have been selected for baselines.|



**42** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



**Process outputs** Implementation approach [Outcome a, b, c, d, e] Constraints on solution [Outcome a] System element (e.g. software) [Outcome b, c] System element (e.g. software) description [Outcome b, c] Requirements imposed on enabling systems [Outcome d] Traceability mapping [Outcome: e] Implementation report [Outcome a, b, c, d, e] Implementation record [Outcome a, b, c, d, e] 

NOTE 1 For software systems, the purpose of the implementation process is to realize a software system element. Software system elements can include hardware, software, and services. For software implementation, this process transforms specified designs, behaviour, interfaces and implementation constraints into actions that create a software system element implemented as a software product or service, also known as a “software item”. Software implementation results in a software element that satisfies specified requirements through verification and stakeholder requirements through validation. Software implementation includes various combinations of construction (coding of newly built software elements), acquisition of new software packages (e.g. from open source or a commercial or organizational source) or re‑use of existing elements (with or without modification). (ISO/IEC/IEEE 12207) 

NOTE 2 Software implementation commonly involves use of the agreement processes to obtain non‑ developmental items (NDI), such as hardware and operating systems (the platform) or enabling systems and services. Software implementation is usually performed concurrently with software integration. Implementation is typically performed along with all of the technical management processes and many of the technical processes, especially: 

- a) the verification process, which provides objective evidence that the software implementation fulfils its specified requirements and identifies anomalies (errors, defects, faults) in implementation-related information items, (e.g. system/software requirements, architecture, design, or other descriptions), processes, software elements, items, units; 

- b) the validation process, which confirms that the implementation fulfils requirements for a specific intended use of a software work product. (ISO/IEC/IEEE 12207) 

###### **5.5.9 Integration process** 

|**Process ID **|**TEC.8**|
|---|---|
|**Process name **|**Integrationprocess**|
|**Process purpose**|The purpose of the integration process is to synthesize a set of system elements<br>into a realized system (product or service) that satisfies system/software re‑<br>quirements, architecture, and design.<br>This process assembles the implemented system elements. Interfaces are identi‑<br>fied and activated to enable interoperation of the system elements as intended.<br>This process integrates the enabling systems with the system‑of‑interest to<br>facilitate interoperation.|



**43** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the integration process:<br>a) Integration constraints that influence system requirements, architecture, or<br>design, including interfaces, are identified.<br>b) Approach and checkpoints for the correct operation of the assembled interfaces<br>and system functions are defined.<br>c) Any enabling systems or services needed for integration are available.<br>d) A system composed of implemented system elements is integrated.<br>e) The interfaces between the implemented system elements that compose the<br>system are checked.<br>f) The interfaces between the system and the external environment are checked.<br>g) Integration results and anomalies are identified.<br>h)Traceabilityof the integrated system elements is established.|
|---|---|
|**Base practices **|**TEC.8.BP1: Prepare for integration.**[Outcome: a, b, c]<br>1) Define the integration strategy.<br>2) Identify and define criteria for integration and points at which the correct<br>operation and integrity of the interfaces and the selected software system func‑<br>tions will be verified.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support integration.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>5) Identify constraints for integration to be incorporated in the system/software<br>requirements, architecture or design.<br>**TEC.8.BP2: Perform integration.**Successively integrate software system ele‑<br>ment configurations until the complete system is synthesized. [Outcome: d, e, f]<br>1) Obtain implemented software system elements in accordance with agreed<br>schedules.<br>2) Integrate the implemented elements.<br>3) Check that the integrated software interfaces or functions run from initiation<br>to an expected termination within an expected range of data values.<br>**TEC.8.BP3: Manage results of integration.**[Outcome: g, h]<br>1) Record integration results and anomalies encountered.<br>2) Maintain traceability of the integrated software system elements.<br>3)Provide keyartefacts and information items that have been selected for baselines.|



**44** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



**Process outputs** Integration approach [Outcome b] Constraints on solution [Outcome a] Integrated system or system element (e.g. software) [Outcome d] System/software interface definition [Outcome: e, f] Requirements imposed on enabling systems [Outcome c] Traceability mapping [Outcome: g] Integration report [Outcome g] Integration record [Outcome a, b, c, d, e, f, g, h] 

NOTE 1 Software system integration iteratively combines implemented software system elements to form complete or partial system configurations in order to build a product or service. Software integration is typically performed daily or continuously during development and maintenance stages, using automated tools. Continuous integration involves frequent inclusion or replacement and archiving of items in software libraries under CM control. (ISO/IEC/IEEE 12207) 

NOTE 2 Interfaces are defined by the architecture definition and design definition processes. The integration process coordinates with these other processes to check that the interface definitions, as implemented and integrated, are adequate and that they take into account the integration needs. (ISO/IEC/IEEE 12207) 

###### **5.5.10 Verification process** 

|**Process ID **|**TEC.9**|
|---|---|
|**Process name **|**Verificationprocess**|
|**Process purpose**|The purpose of the verification process is to provide objective evidence that a<br>system or system element fulfils its specified requirements and characteristics.<br>The verification process identifies the anomalies (errors, defects, or faults) in any<br>information item (e.g. system/software requirements or architecture descrip‑<br>tion), implemented system elements, or life cycle processes using appropriate<br>methods, techniques, standards or rules. This process provides the necessary<br>information to determine resolution of identified anomalies.|
|**Process outcomes**|As a result of the successful implementation of the verification process:<br>a) Constraints of verification that influence the requirements, architecture, or<br>design are identified.<br>b) Any enabling systems or services needed for verification are available.<br>c) The system or system element is verified.<br>d) Data providing information for corrective actions is reported.<br>e) Objective evidence that the realized system fulfils the requirements, archi‑<br>tecture and design is provided.<br>f) Verification results and anomalies are identified.<br>g)Traceabilityof the verified system elements is established.|



**45** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.9.BP1: Prepare for verification.**[Outcome: a, b]<br>1) Define the verification strategy.<br>2) Identify constraints from the verification strategy to be incorporated in the<br>system/software requirements, architecture, or design.<br>3) Define the purpose, conditions and conformance criteria for each verification<br>action.<br>4) Select appropriate verification methods or techniques and associated criteria<br>for verification actions, such as inspection, analysis, demonstration, or testing.<br>5) Identify and plan for the necessary enabling systems or services needed to<br>support verification.<br>6) Obtain or acquire access to the enabling systems or services to be used to<br>support verification.<br>**TEC.9.BP2: Perform verification.**[Outcome: c, e, f]<br>1) Define the verification procedures, each supporting one or a set of verification<br>actions.<br>2) Perform the verification procedures.<br>**TEC.9.BP3: Manage results of verification.**[Outcome: d, e, f, g]<br>1) Review verification results and anomalies encountered and identify follow-up<br>actions.<br>2) Record incidents and problems during verification and track their resolution.<br>3) Obtain stakeholder agreement that the software system or element meets the<br>specified requirements.<br>4) Maintain traceability of the verified software system elements.<br>5)Provide keyartefacts and information items that have been selected for baselines.|
|---|---|
|**Process outputs**|Verification approach [Outcome a, b, c, d, e, f, g]<br>Constraints on solution [Outcome a]<br>Verification criteria [Outcome: e]<br>Verified system/software [Outcome c]<br>Requirements imposed on enabling systems [Outcome b]<br>Traceability mapping [Outcome: g]<br>Verification report [Outcome d, e, f]|
||Verification record[Outcome a, b, c, d, e, f,g]|



NOTE 1 Verification can be performed across all technical processes. The verification process is typically used at key points in a software system’s life cycle to demonstrate that the requirements (including functional and non‑functional requirements) have been met, or that process outcomes have been achieved or process activities have been performed. Different domains and engineering or development communities can identify the milestones, verification strategies and criteria differently. (ISO/IEC/IEEE 12207) 

- NOTE 2 For software systems, the verification process is typically instantiated for the following purposes: 

- a) to confirm that a software work product or service properly reflects the specified requirements (often called software verification); 

- b) to confirm that the integrated software product meets its defined requirements (often called software qualification testing); 

- c) to confirm that the implementation of each system/software requirement is tested for compliance and that the software system is ready for delivery (often called system qualification testing). (ISO/IEC/IEEE 12207) 

**46** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



NOTE 3 The verification process determines that the “product is built right”. The validation process determines that the “right product is built”. (ISO/IEC/IEEE 12207) 

NOTE 4 ISO/IEC/IEEE 29119 provides detailed processes and techniques for verification performed through testing. IEEE 1012‑2012 provides additional details about these processes for systems, software, hardware, and interfaces being developed, maintained, or reused. (ISO/IEC/IEEE 12207) 

NOTE 5 The SWEBOK, Guide to the Software Engineering Body of Knowledge, provides detailed discussion on software testing. This knowledge area addresses fundamentals, terminology, issues, techniques, application, process planning, measures, tools, practical considerations, and references. The guide also discusses software verification and validation in terms of software quality management processes, and identifies methods and techniques that support both verification and validation. The SWEBOK also addresses topics such as software construction for verification and software engineering models and methods support. (ISO/IEC/IEEE 12207) 

###### **5.5.11 Transition process** 

|**Process ID **|**TEC.10**|
|---|---|
|**Process name **|**Transitionprocess**|
|**Process purpose**|The purpose of the transition process is to establish a capability for a system<br>to provide services specified by stakeholder requirements in the operational<br>environment.<br>This process moves the system in an orderly, planned manner into the operational<br>status, such that the system is functional, operable and compatible with other<br>operational systems. It installs a verified system, together with relevant enabling<br>systems, e.g. planning system, support system, operator training system, user<br>training system, as defined in agreements. This process is used at each level in<br>the system structure and in each stage to complete the criteria established for<br>exiting the stage. It includes preparing applicable storage, handling, and shipping<br>enablingsystems.|
|**Process outcomes**|As a result of the successful implementation of the transition process:<br>a) Transition constraints that influence system/software requirements, archi‑<br>tecture, or design are identified.<br>b) Any enabling systems or services needed for transition are available.<br>c) The site is prepared.<br>d) The system, as installed in its operational location, is capable of delivering its<br>specified functions.<br>e) Operators, users and other stakeholders necessary to the system utilization<br>and support are trained.<br>f) Transition results and anomalies are identified.<br>g) The installed system is activated and ready for operation.<br>h)Traceabilityof the transitioned elements is established.|



**47** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.10.BP1: Prepare for software system transition.**[Outcome: a, b, c]<br>1) Define a strategy for managing software releases and other software system<br>transitions.<br>2) Identify and define facility, site, communications network, or target environ‑<br>ment changes needed for software system installation or transition.<br>3) Identify information needs and arrange for user documentation and training<br>of operators, users, and other stakeholders necessary for system utilization and<br>support.<br>4) Prepare detailed transition information, such as plans, schedules, and pro‑<br>cedures.<br>5) Identify system constraints from transition to be incorporated in the software<br>system requirements, architecture or design.<br>6) Identify and plan for the necessary enabling systems or services needed to<br>support transition.<br>7) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.10.BP2: Perform the transition.**[Outcome: c, d, e, g]<br>1) Prepare the site of operation or virtual environment in accordance with in‑<br>stallation requirements.<br>2) Deliver the software system or element for installation at the correct location<br>and time.<br>3) Install the product in its physical or virtual operational location and interface<br>to its environment.<br>4) Provide user documentation and training for the operators, users, and other<br>stakeholders necessary for product utilization and support.<br>5) Perform activation and check‑out.<br>**TEC.10.BP3: Manage results of transition.**[Outcome: f, h]<br>1) Record transition results and anomalies encountered.<br>2) Record transition incidents and problems and track their resolution.<br>3) Maintain traceability of the transitioned software system elements.<br>4)Provide keyartefacts and information items that have been selected for baselines.|
|---|---|



**48** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



**Process outputs** Transition approach [Outcome a] Constraints on solution [Outcome a] Installed system/software [Outcome c, d, g] Requirements imposed on enabling systems [Outcome b] Traceability mapping [Outcome: h] Transition report [Outcome f] Transition record [Outcome a, b, c, d, e, f, g, h] 

NOTE 1 For software systems, the purpose of the transition process is to establish a capability for a system to provide services in a different environment. The transition process is often used for recurring deployments of software to different environments, e.g. from a development environment to a test or maintenance environment, or between various test environments, or from one operational environment to another (e.g. rehosting or use of cloud services). Transitions to backup or contingent sites are typically planned and rehearsed for business continuity and disaster recovery. Transition for software systems can involve the physical relocation of hardware, the installation and activation or deactivation of physical or virtual infrastructure or enabling systems in different locations, or no change to the physical infrastructure. Transition can involve changes to the data sources, data structure, or updates or upgrades of functional software. Transition includes recurring scheduled or emergency patches and fixes for security and other concerns. Transition can involve transfer between organizations and also encompasses the addition of a large group of new users to an existing software system or service. Transition to a new system often is performed concurrently with retirement and disposal of an existing system, entailing data migration from the old system to its replacement. (ISO/IEC/IEEE 12207) 

NOTE 2 Transition can involve knowledge transfer using the knowledge management process. (ISO/IEC/IEEE 12207) 

###### **5.5.12 Validation process** 

|**Process ID **|**TEC.11**|
|---|---|
|**Process name **|**Validationprocess**|
|**Process purpose**|The purpose of the validation process is to provide objective evidence that the<br>system, when in use, fulfils its business or mission objectives and stakeholder<br>requirements, achieving its intended use in its intended operational environment.<br>The objective of validating a system or system element is to acquire confidence<br>in its ability to achieve its intended mission, or use, under specific operational<br>conditions. Validation is ratified by stakeholders. This process provides the neces‑<br>sary information so that identified anomalies can be resolved by the appropriate<br>technicalprocess where the anomalywas created.|
|**Process outcomes**|As a result of the successful implementation of the validation process:<br>a) Validation criteria for stakeholder requirements are defined.<br>b) The availability of services required by stakeholders is confirmed.<br>c) Constraints of validation that influence the requirements, architecture, or<br>design are identified.<br>d) The system or system element is validated.<br>e) Any enabling systems or services needed for validation are available.<br>f) Validation results and anomalies are identified.<br>g) Objective evidence that the realized system or system element satisfies stake‑<br>holder needs is provided.<br>h)Traceabilityof the validated system elements is established.|



**49** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.11.BP1: Prepare for validation.**[Outcome: a, b, c, e]<br>1) Define the validation strategy.<br>2) Identify system constraints from the validation strategy to be incorporated<br>in the stakeholder requirements.<br>3) Define the purpose, conditions and conformance criteria for each validation<br>action.<br>4) Select appropriate validation methods or techniques and associated criteria<br>for each validation action.<br>5) Identify and plan for the necessary enabling systems or services needed to<br>support validation.<br>6) Obtain or acquire access to the enabling systems or services to be used to<br>support validation.<br>**TEC.11.BP2: Perform validation.**[Outcome: b, d, f]<br>1) Define the validation procedures, each supporting one or a set of validation<br>actions.<br>2) Perform the validation procedures in the defined environment.<br>**TEC.11.BP3: Manage results of validation.**[Outcome: f, g, h]<br>1) Review validation results and anomalies encountered and identify follow‑up<br>actions.<br>2) Record incidents and problems during validation and track their resolution.<br>3) Obtain stakeholder agreement that the system or system element meets the<br>stakeholder needs.<br>4) Maintain traceability of the validated system elements.|
|---|---|
||5)Provide keyartefacts and information items that have been selected for baselines.|
|**Process outputs**|Validation approach [Outcome a, c]<br>Constraints on solution [Outcome c]<br>Validation criteria [Outcome: a]<br>Validated system/software [Outcome b, d]<br>Requirements imposed on enabling systems [Outcome e]<br>Traceability mapping [Outcome: h]<br>Validation report [Outcome f, g]|
||Validation record[Outcome a, b, e, f,g]|



NOTE 1 The validation process is typically used at key points in a product’s life cycle to demonstrate that the product’s requirements for stakeholder intended operational use have been met. Validation is also applicable to the software engineering artefacts (viewed as software system elements). Different domains and engineering or development communities can identify the milestones, validation strategies and criteria differently. For software systems, highly iterative life cycle models often feature frequent involvement by the acquirer, user representative, or other stakeholders to validate, e.g. the priority of requirements for inclusion in an iteration, the usability of the software interface through prototypes, and the suitability of the software for performing business tasks and fulfilling the operational concept. (ISO/IEC/IEEE 12207) 

- NOTE 2 For software systems, the following are purposes of the validation process: 

- a) to confirm that the requirements for a specific intended use of the software work product are fulfilled (often called software validation); 

- b) to achieve confidence (especially with an acquirer or customer) that the delivered product meets stakeholder requirements and is fit for use (often called software acceptance testing). (ISO/IEC/IEEE 12207) 

**50** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



NOTE 3 The validation process determines that the “right product is built”. The verification process determines that the “product is built right”. (ISO/IEC/IEEE 12207) 

NOTE 4 Acceptance criteria, as used for acceptance testing, include criteria to determine whether the delivered product is fit to use or not. Acceptance criteria for acceptance can be specified and agreed between two parties, i.e., an acquirer and a supplier, and included in the stakeholder requirements. (ISO/IEC/IEEE 12207) 

NOTE 5 IEEE 1012‑2012 provides detailed requirements. The SWEBOK, Guide to the Software Engineering Body of Knowledge, discusses software verification and validation in terms of software quality management processes, and contains methods and techniques that support both verification and validation. The SWEBOK also addresses topics such as requirements and model validation. (ISO/IEC/IEEE 12207) 

###### **5.5.13 Operation process** 

|**Process ID **|**TEC.12**|
|---|---|
|**Process name **|**Operationprocess**|
|**Process purpose**|The purpose of the operation process is to use the system to deliver its services.<br>This process establishes requirements for and assigns personnel to operate the<br>system, and monitors the services and operator‑system performance. In order<br>to sustain services, it identifies and analyses operational anomalies in relation<br>to agreements, stakeholder requirements and organizational constraints.|
|**Process outcomes**|As a result of the successful implementation of the operation process:<br>a) Operation constraints that influence system/software requirements, archi‑<br>tecture, or design are identified.|
||b) Any enabling systems, services, and material needed for operation are available.<br>c) Trained, qualified operators are available.<br>d) System product services that meet stakeholder requirements are delivered.<br>e) System product performance during operation is monitored.<br>f)Support to the customer isprovided.|



**51** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices **|**TEC.12.BP1: Prepare for operation.**[Outcome: a, b, c]<br>1) Define an operation strategy.<br>2) Identify system constraints from operation to be incorporated in changes to<br>the system/software requirements, architecture, design, implementation, or<br>transition.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support operation.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>5) Identify or define training and qualification requirements for personnel needed<br>for software system operation.<br>6) Depending on the need for human intervention and control of operations,<br>assign trained, qualified personnel to be operators.<br>**TEC.12.BP2: Perform operation.**[Outcome: d, e, f]<br>1) Use the software system in its intended operational environment.<br>2) Apply materials and other resources, as required, to operate the software<br>system and sustain its services.<br>3) Monitor software system operation.<br>4) Consistent with the operational strategy, develop and, where feasible, automate<br>operational procedures to minimize the risk of operational anomalies.<br>5) Consistent with the operational strategy, analyse measurements to confirm<br>that service performance is within acceptable parameters.<br>6) Perform contingency operations, if necessary.<br>**TEC.12.BP3: Manage results of operation.**[Outcome: e]<br>1) Record results of operation and anomalies encountered.<br>2) Record operational incidents and problems and track their resolution.<br>3) Maintain traceability of the operational services and configuration items.<br>4) Provide key artefacts and information items that have been selected for baselines.<br>**TEC.12.BP4: Support the customer.**[Outcome: d, e, f]<br>1) Provide assistance and consultation to the customers and users to resolve<br>complaints, incidents, problems, and service requests.<br>2) Record and monitor requests and subsequent actions for support.<br>3) Determine the degree to which delivered software system or services satisfy<br>the needs of the customers and users.|
|---|---|



**52** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



**Process outputs** Operation approach [Outcome a] Constraints on solution [Outcome a] Trained operator [Outcome c] Operational system/software [Outcome d, f] Requirements imposed on enabling systems [Outcome b] Traceability mapping [Outcome: e] Operation report [Outcome e] Operation record [Outcome a, b, c, d, e, f] 

NOTE 1 The operation process typically aims to control or reduce the cost of operations while sustaining an acceptable or improved level of service. Software systems can have dedicated infrastructure, but are typically operated in distributed environments where other software systems and services (e.g. the internet) are active. The security, availability, and operational performance of the software system‑of‑interest are thus a matter of concern within a larger system of systems. It can include coordination with pre‑existing, concurrent or continuing services delivered by other systems that provide identical or similar services. (ISO/IEC/IEEE 12207) 

NOTE 2 <u>ISO/IEC 20000‑1 is a service management system standard that specifies requirements for the design,</u> transition, delivery and improvement of managed operational services, and supports the operation process to achieve its purpose. (ISO/IEC/IEEE 12207) 

###### **5.5.14 Maintenance process** 

|**Process ID **|**TEC.13**|
|---|---|
|**Process name **|**Maintenanceprocess**|
|**Process purpose**|The purpose of the maintenance process is to sustain the capability of the system<br>to provide a service.<br>This process monitors the system’s capability to deliver services, records incidents<br>for analysis, takes corrective, adaptive, perfective and preventive actions and con‑<br>firms restored capability.|
|**Process outcomes**|As a result of the successful implementation of the maintenance process:<br>a) Maintenance constraints that influence system requirements, architecture, or<br>design are identified.<br>b) Any enabling systems or services needed for maintenance are available.<br>c) Replacement, repaired, or revised system elements are made available.<br>d) The need for changes to address corrective, perfective, or adaptive maintenance<br>is reported.|
||e)Failure and lifetime data, includingassociated costs, is determined.|



**53** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Base practices**|**TEC.13.BP1: Prepare for maintenance.**[Outcome: a, b]<br>1) Define a maintenance strategy.<br>2) For non-software elements, define a logistics strategy throughout the life cycle,<br>including acquisition and operational considerations: the number and type of<br>replacement elements to be stored, their storage locations and conditions, their<br>anticipated replacement rate, and their storage life and renewal frequency.|
|---|---|
||3) Identify constraints from maintenance to be incorporated in the system/software<br>requirements, architecture, or design.|
||4) Identify trades such that the system and associated maintenance and logistics<br>actions results in a solution that is affordable, operable, supportable, and sustainable.<br>5) Identify and plan for the necessary enabling systems or services needed to sup‑<br>port maintenance.<br>6) Obtain or acquire access to the enabling systems or services to be used.<br>**TEC.13.BP2: Perform maintenance.**[Outcome: c, d, e]<br>1) Review stakeholder requirements, complaints, events, incident and problem re‑<br>ports to identify corrective, adaptive, perfective and preventive maintenance needs.|
||2) Analyse the impact of maintenance changes on data structures, data, and related<br>software functions, user documentation, and interfaces.|
||3) Upon encountering unexpected faults that cause a software system failure, re‑<br>store the system to operational status.<br>4) Implement the procedures for correction of flaws (defects) and errors, or for<br>replacement or upgrade of system elements.<br>5) Perform preventive maintenance by replacing, patching, augmenting, or upgrad‑<br>ing software system elements, to improve the performance of a software system<br>that is projected to reach unacceptable service levels, e.g. lack of capacity due to<br>increases in demand or stored data, or to avoid unacceptable operating conditions,<br>e.g. running with outdated security software.<br>6) Identify when adaptive or perfective maintenance is required.<br>**TEC.13.BP3: Perform logistics support.**[Outcome: b, c]|
||1) Obtain resources to support the software system through its life cycle or the<br>project’s life (acquisition logistics).|
||2) Monitor the quality and availability of replacement elements and enabling systems,<br>their delivery mechanisms and their continued integrity during storage.|
||3) Implement mechanisms for software system or element distribution, including<br>packaging, handling, storage and communications or transportation needed for<br>items during the life cycle.|
||4) Confirm that logistics actions to fulfil software system or element supportability<br>requirements or achieve operational readiness are planned and implemented.<br>**TEC.13.BP4: Manage results of maintenance and logistics**. [Outcome: d, e]<br>1) Record incidents and problems, including their resolutions, and significant main‑<br>tenance and logistics results.|
||2) Identify and record trends of incidents, problems, and maintenance and logistics<br>actions.<br>3) Maintain traceability of the system elements being maintained.<br>4) Provide key artefacts and information items that have been selected for baselines.<br>5)Monitor and measure customer satisfaction with system and maintenance support.|



**54** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outputs**|Maintenance approach [Outcome a]|
|---|---|
||Constraints on solution [Outcome a]<br>Trained maintainer [Outcome b]|
||Maintained system/software [Outcome c]|
||Requirements imposed on enabling systems [Outcome b]|
||Traceability mapping [Outcome: d]|
||Maintenance report [Outcome d, e]|
||Maintenance record[Outcome a, b, c, d, e]|



NOTE 1 For software systems, the maintenance process makes corrections, changes, and improvements to deployed software systems and elements. The software systems maintenance approach differs for systems that are freely available, in wide commercial distribution, or operating in a small number of controlled environments. The need for software system maintenance can arise from multiple causes other than latent system defects, such as changes to interfaced systems or infrastructure, evolving security threats, and technical obsolescence of system elements and enabling systems over the system life cycle. Often the extension of capability, mid‑life upgrade, or evolution of legacy systems becomes a new software system development project that will apply the set of processes within an appropriate life cycle. If so, the portfolio management process is the starting point to initiate the work. In other cases, software system maintenance is performed as a continuing series of prioritized work items, possibly on a level of effort basis. Maintenance of software system elements can include hardware, software, and services, such as communication or web services. Maintenance is closely connected with the configuration management process and software asset management and is performed concurrently with the other technical processes. (ISO/IEC/IEEE 12207) 

NOTE 2 ISO/IEC/IEEE 14764 and <u>ISO/IEC 16350</u> provide additional detail. The SWEBOK, Guide to the Software Engineering Body of Knowledge, Software Maintenance knowledge area discusses software maintenance fundamentals, key issues, measurement, techniques, maintenance process and support activities, and tools. The guide also discusses models, techniques and measures that support software reliability. (ISO/IEC/IEEE 12207) 

###### **5.5.15 Disposal process** 

|**Process ID **|**TEC.14**|
|---|---|
|**Process name **|**Disposalprocess**|
|**Process purpose**|The purpose of the disposal process is to end the existence of a system element<br>or system for a specified intended use, appropriately handle replaced or retired<br>elements, and to properly attend to identified critical disposal needs (e.g. per an<br>agreement, per organizational policy, or for environmental, legal, safety, security<br>aspects).|
||This process deactivates, disassembles and removes the system or any of its sys‑<br>tem elements from the specific use. It addresses any waste products, consigning<br>them to a final condition and returning the environment to its original or an<br>acceptable condition. The waste products can be in‑process resulting during any<br>life cycle stage, e.g. waste materials during fabrication. This process destroys,<br>stores or reclaims system elements and waste products in an environmentally<br>sound manner, in accordance with legislation, agreements, organizational con‑<br>straints and stakeholder requirements. Disposal includes preventing expired,<br>non‑reusable, or inadequate elements from getting back into the supply chain.<br>Where required, it maintains records in order that the health of operators and<br>users, and the safety of the environment, can be monitored. When part of the<br>system will continue to be in use in a modified form, the disposal process helps<br>ensure theproper handlingof theportion beingretired.|



**55** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process outcomes**|As a result of the successful implementation of the disposal process:<br>a) Disposal constraints are provided as inputs to requirements, architecture,<br>design, and implementation.<br>b) Any enabling systems or services needed for disposal are available.<br>c) The system elements or waste products are destroyed, stored, reclaimed or<br>recycled in accordance with requirements, e.g. safety and security requirements.<br>d) The environment is returned to its original or an agreed state.|
|---|---|
||e)Records of disposal actions and analysis are available.|
|**Base practices **|**TEC.14.BP1: Prepare for disposal.**[Outcome: a, b]<br>1) Define a disposal strategy for the software system, to include each system<br>element and to identify and address critical disposal needs.<br>2) Identify constraints on disposal for the system/software requirements, archi‑<br>tecture and design characteristics, or implementation techniques.<br>3) Identify and plan for the necessary enabling systems or services needed to<br>support disposal.<br>4) Obtain or acquire access to the enabling systems or services to be used.<br>5) Specify containment facilities, storage locations, inspection criteria and storage<br>periods, if the software system or data is to be stored, consistent with security<br>and environmental considerations.<br>6) Define preventive methods to preclude disposed elements and materials that<br>should not be repurposed, reclaimed or reused from re‑entering the supply chain.<br>**TEC.14.BP2: Perform disposal.**[Outcome: c]<br>1) Deactivate the software system or element to prepare it for removal.<br>2) Remove the software system, its elements, its data, and non‑reusable material<br>from use or production for appropriate disposition and action.<br>3) Withdraw impacted operating staff from the software system or system ele‑<br>ment and record relevant operating knowledge.<br>4) Reuse, recycle, recondition, overhaul, archive, or destroy designated software<br>system elements.<br>5) Conduct destruction of the system elements, as necessary, to reduce the amount<br>of waste treatment or to make the waste easier to handle.<br>**TEC.14.BP3: Finalize the disposal.**[Outcome: d, e]<br>1) Confirm that detrimental health, safety, security, and environmental conditions<br>following disposal have been identified and treated.<br>2) Return the environment to its original state or to a state that specified by<br>agreement.<br>3) Archive information gathered through the lifetime of the product to permit<br>audits and reviews in the event of long‑term hazards to health, safety, security<br>and the environment, and to permit future software system creators and users<br>to build a knowledge base from experience.|



**56** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



**Process outputs** Disposal approach [Outcome a] Constraints on solution [Outcome a] Disposed system/software [Outcome c, d] Requirements imposed on enabling systems [Outcome b] Traceability mapping [Outcome: c] Disposal report [Outcome a, c] Disposal record [Outcome e] 

NOTE 1 Disposal of software systems encompasses the termination of services and disposal of software elements, stored data, media and firmware, information items, and associated hardware elements that will not be reused or transitioned to another system. The disposal process is intended to be applicable in any stage of a software systems life cycle. For software, the disposal process applies throughout the life cycle to source code or executable copies of the software, personally identifiable or controlled data used in the software system, and associated information items, retained under centralized configuration control or distributed for use, e.g. disposing of prototypes in early life cycle stages, and decommissioning elements replaced from modifications during utilization/deployment and support stages. When the system-of-interest is being modified for technology or capability upgrades, only the impacted elements are deactivated and removed. (ISO/IEC/IEEE 12207) 

NOTE 2 The business or mission analysis process and decision management process are typically applied to address the impact on stakeholders of system disposal and potential new system capabilities. (ISO/IEC/IEEE 12207) 

#### **6 The quality dimension** 

A process assessment model shall incorporate a process measurement framework conformant with the requirements of <u>ISO/IEC 33003</u> and is expressed as a process quality characteristic with a defined set of process attributes. At minimum, a process measurement framework includes a process quality attribute of process performance, which is needed to demonstrate that the process achieves its expected process outcomes. Other process quality attributes may be added over the process performance attribute. 

NOTE 1 <u>ISO/IEC 33020 provides a process measurement framework for the assessment of process capability</u> which can be incorporated into this document. <u>ISO/IEC 33020 also includes a set of process quality indicators for</u> each process attribute in the process measurement framework. 

The assessment indicators are used as a basis for collecting objective evidence to support an assessor’s judgement in assigning ratings of the performance and quality of an implemented process. The set of indicators defined in this document are not intended to be an all-inclusive set and applicable in its entirety. Subsets appropriate to the context and scope of the assessment should be selected, and potentially augmented with additional indicators. 

A process assessment is conducted according to a documented assessment process. A documented assessment process identifies the rating method to be used in rating process attributes and identifies or defines the aggregation method to be used in determining ratings. 

NOTE 2 <u>ISO/IEC 33020</u> includes a process attribute rating scale, process attribute rating method, and aggregation method which can provide a suitable basis for use for incorporating into any documented assessment process. 

**57** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



### **Annex A** (informative) **Process outputs** 

#### **A.1 Process output descriptions** 

The process outputs associated with the processes in <u>Clause 5</u> are described in <u>Table A.1. The</u> descriptions are exemplary. The process outputs are identified by categories which are defined in A.2. The corresponding processes of the process outputs are indicated by the process IDs. 

NOTE For further guidance, <u>ISO/IEC/IEEE 15289</u> addresses the content for life cycle process information items (documentation). 

**Table A.1 — Process output descriptions** 

|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Accepted system or<br>system element (e.g.<br>software)|System element or system is transferred from supplier<br>to acquirer and the product or service is available to<br>theproject.[INCOSE SE Handbook 2015]|<br> <br>product|AGR.1|
|Acquisition agreement|The formal agreement between an acquirer and a<br>supplier. Informally, commitments or agreements may<br>be specified between an acquirer and a supplier of the<br>same organization (sometimes called a memorandum<br>of understanding).[Adapted from ISO/IEC/IEEE 15289]|<br> <br> <br> <br>agreement|AGR.1|
|Acquisition agreement<br>change request|Requests from an acquirer to change an agreement<br>with a supplier.|<br>request|AGR.1|
|Acquisition approach|Specific approach to acquiring products and services<br>that is based on considerations of supply sources, ac‑<br>quisition methods, requirements specification types,<br>contract or agreement types, and related acquisition<br>risks.[ISO/IEC/IEEE 24765]|<br> <br> <br>plan|AGR.1|
|Acquisition need|The identification of a need that cannot be met within<br>the organization encountering the need or a need that<br>can be met in a more economical way by a supplier.<br>[INCOSE SE Handbook 2015]|<br> <br> <br>specification|MAN.1|
|Acquisition record|Permanent, readable form of data, information, or knowl‑<br>edge related to acquisition.[INCOSE SE Handbook 2015]|record|AGR.1|
|Acquisition report|An account prepared for interested parties in order<br>to communicate the status, results, and outcomes of<br>the acquisition activities.[INCOSE SE Handbook 2015]|<br> <br>report|AGR.1|
|Alternative solution<br>classes|Identifies and describes the classes of solutions that<br>may address the problem or opportunity. [INCOSE SE<br>Handbook 2015]|<br> <br>description|TEC.1|
|Architecture defini‑<br>tion approach|Approaches, schedules, resources, and specific consider‑<br>ations required to define the selected system/software<br>architecture that satisfies the requirements. [Adapted<br>from INCOSE SE Handbook 2015]|<br> <br>plan|TEC.4|
|Architecture defini‑<br>tion record|Permanent, readable form of data, information, or<br>knowledge related to architecture definition. [INCOSE<br>SE Handbook 2015]|<br> <br>record|TEC.4|



**58** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Business or mission<br>analysis approach|Approaches, schedules, resources, and specific con‑<br>siderations required to conduct business or mission<br>analysis and ensure business needs are elaborated<br>and formalized into business requirements. [INCOSE<br>SE Handbook 2015]|plan|TEC.1|
|Business or mission<br>analysis record|Permanent, readable form of data, information, or<br>knowledge related to business or mission analysis.<br>[INCOSE SE Handbook 2015]|record|TEC.1|
|Configuration audit<br>result|Artefacts that are expected through conduct of config‑<br>uration audit and that can be considered elements of<br>exit criteria[Adapted from IEEE 15288.2‑2014]|record|MAN.5|
|Configuration baseline|Configuration information formally designated at<br>a specific time during the life of a product, product<br>component, service, or service component. [ISO/IEC/<br>IEEE 24765]|record|MAN.5|
|Configuration evalu‑<br>ation report|Provides results of configuration management evalu‑<br>ations. It includes evaluation criteria. [Adapted from<br>ISO/IEC/IEEE 15289]|report|MAN.5|
|Configuration man‑<br>agement approach|Describes the responsible organization for authorizing<br>and performing configuration management activities,<br>and their relationship with other organizations. [Adapted<br>fromISO/IEC/IEEE 15289]|plan|MAN.5|
|Configuration man‑<br>agement change re‑<br>quest|Identifies a problem, maintenance need, or desired im‑<br>provement and requests modifications. The requested<br>change may affect a contract, configuration item, sys‑<br>tem, service, hardware, software, interface, asset, or<br>documentation.[Adapted fromISO/IEC/IEEE 15289]|request|MAN.5|
|Configuration man‑<br>agement record|Permanent, readable form of data, information, or<br>knowledge related to configuration management.<br>[INCOSE SE Handbook 2015]|record|MAN.5|
|Configuration man‑<br>agement report|Provides the status of controlled configuration items,<br>including baselines, release identifiers, and location of<br>the configuration item master version. For deactivat‑<br>ed systems/software, it contains information about<br>system/software disposal to trace potential future<br>environmental, safety, or security impacts. [Adapted<br>fromISO/IEC/IEEE 15289]|report|MAN.5|
|Configuration man‑<br>agement system|System used to support and enable configuration<br>management.|product|MAN.5|
|Configuration man‑<br>agement variance re‑<br>quest|Request to accept a configuration item or other desig‑<br>nated item which, during production or after having<br>been submitted for inspection, is found to depart from<br>specified requirements, but is nevertheless considered<br>suitable for use as is or after rework by an approved<br>method.[Adapted from ISO/IEC/IEEE 24765]|request|MAN.5|
|Constraints on solu‑<br>tion|Externally imposed limitation on system requirements,<br>design, or implementation or on the process used to<br>develop or modify a system/software. [Adapted from<br>ISO/IEC/IEEE 29148]|specification|TEC.7, TEC.8, TEC.9,<br>TEC .10, TEC .11,<br>TEC.12, TEC.13,<br>TEC.14|
|Critical performance<br>data|<br>Data provided for the identified system of interest<br>(including software as a system) measurement needs.<br>[Adapted from INCOSE SE Handbook 2015]|data|TEC.2, TEC.3, TEC.4,<br>TEC.5|
|Critical performance<br>measurement needs|Identification of information needs of the decision<br>makers with respect to system of interest (including<br>software as a system) expectations. [Adapted from<br>INCOSE SE Handbook 2015]|specification|TEC.2, TEC.3, TEC.4,<br>TEC.5|



**59** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Decision management<br>approach|Approaches, schedules, resources, and specific consid‑<br>erations required to perform decision management for<br>aproject.[INCOSE SE Handbook 2015]|<br>plan|MAN.3|
|Decision management<br>record|Permanent, readable form of data, information, or<br>knowledge related to decision management. [INCOSE<br>SE Handbook 2015]|<br> <br>record|MAN.3|
|Decision management<br>report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>decision management activities. [INCOSE SE Handbook<br>2015]|<br> <br> <br>report|MAN.3|
|Decision register|A repository that supports the availability for use and<br>communication of all relevant decision information in<br>a timely, complete, valid, and, if required, confidential<br>manner.[Adapted from INCOSE SE Handbook 2015]|<br> <br> <br>registry|MAN.3|
|Design definition ap‑<br>proach|Approaches, schedules, resources, and specific consid‑<br>erations required to define the system/software design<br>that is consistent with the selected system/software<br>architecture and satisfies the requirements. [Adapted<br>from INCOSE SE Handbook 2015]|<br> <br> <br>plan|TEC.5|
|Design definition re‑<br>cord|Permanent, readable form of data, information, or<br>knowledge related to design definition. [INCOSE SE<br>Handbook 2015]|<br> <br>record|TEC.5|
|Disposal approach|Presents how activities are conducted to retire sys‑<br>tems/software or services and related documents. It<br>identifies stakeholders and user organizations or users<br>to be notified of the planned withdrawal from service,<br>replacement systems/software and services, if any; a<br>schedule for cessation of support. [Adapted fromISO/<br>IEC/IEEE 15289]|<br> <br> <br> <br>plan|TEC.14|
|Disposal record|Permanent, readable form of data, information, or knowl‑<br>edge related to disposal.[INCOSE SE Handbook 2015]|record|TEC.14|
|Disposal report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>disposal activities.[INCOSE SE Handbook 2015]|<br> <br>report|TEC.14|
|Disposed system/<br>software|System/software that has been deactivated, disassem‑<br>bled, and removed from operations. [Adapted from<br>INCOSE SE Handbook 2015]|<br>product|TEC.14|
|Human resource man‑<br>agement record|Permanent, readable form of data, information, or<br>knowledge related to human resource management.<br>[INCOSE SE Handbook 2015]|<br> <br>record|ORG.4|
|Human resource man‑<br>agement report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>human resource management activities. [INCOSE SE<br>Handbook 2015]|<br> <br> <br>report|ORG.4|
|Human resource man‑<br>agement strategy|Approaches, schedules, resources, and specific con‑<br>siderations required to identify the skill needs of the<br>organization and projects. Includes the organizational<br>training plan needed to develop internal personnel<br>and the acquisition of external personnel. [INCOSE SE<br>Handbook 2015]|<br> <br> <br> <br>plan|ORG.4|
|Human resource re‑<br>quirements|Identification and documentation of organization‑<br>al human resource needs. [Adapted from ISO/IEC/<br>IEEE 24765]|specification|ORG.4|



**60** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Implementation ap‑<br>proach|Approaches, schedules, resources, and specific con‑<br>siderations required to realize system elements (e.g.<br>software) to satisfy system requirements, architecture,<br>and design.[INCOSE SE Handbook 2015]|<br> <br>plan|TEC.7|
|Implementation re‑<br>cord|Permanent, readable form of data, information, or<br>knowledge related to implementation. [INCOSE SE<br>Handbook 2015]|<br> <br>record|TEC.7|
|Implementation report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>implementation activities.[INCOSE SE Handbook 2015]|<br> <br>report|TEC.7|
|Information manage‑<br>ment approach|Presents how the system or service provider plans to<br>conduct information management activities during the<br>life cycle.[Adapted fromISO/IEC/IEEE 15289]|<br> <br>plan|MAN.6|
|Information manage‑<br>ment record|Permanent, readable form of data, information, or<br>knowledge related to information management. [INCOSE<br>SE Handbook 2015]|<br> <br>record|MAN.6|
|Information manage‑<br>ment report|An account prepared for interested parties in order<br>to communicate the status, results, and outcomes of<br>the information management activities. [INCOSE SE<br>Handbook 2015]|<br> <br> <br>report|MAN.6|
|Information register|A repository that supports the availability for use and<br>communication of all relevant project information<br>artefacts in a timely, complete, valid, and, if required,<br>restricted manner. [Adapted from INCOSE SE Hand‑<br>book 2015]|<br> <br> <br>registry|MAN.6|
|Infrastructure change<br>requests|Requests to change the organizational infrastructure.|request|ORG.2|
|Infrastructure man‑<br>agement record|Permanent, readable form of data, information, or<br>knowledge related to infrastructure management.<br>[INCOSE SE Handbook 2015]|<br> <br>record|ORG.2|
|Infrastructure man‑<br>agement report|An account prepared for interested parties in order<br>to communicate the status, results, and outcomes of<br>the infrastructure management activities. [INCOSE SE<br>Handbook 2015]|<br> <br> <br>report|ORG.2|
|Infrastructure man‑<br>agement strategy|Approaches, schedules, resources, and specific consider‑<br>ations required to define and sustain the organizational<br>andproject infrastructures.[INCOSE SE Handbook 2015]|<br>plan|ORG.2|
|Infrastructure re‑<br>quirements|Identification and documentation of project roles, re‑<br>sponsibilities and reporting relationships, as well as<br>estimation of required staff by time period and creation<br>of a staffingmanagementplan.[ISO/IEC/IEEE 24765]|<br> <br>specification|ORG.2|
|Installed system/soft‑<br>ware|System/software that has been installed in its opera‑<br>tional environment.|product|TEC.10|
|Integrated system or<br>system element (e.g.<br>software)|Integrated system element (e.g. software) or system<br>ready for verification. The resulting aggregation of<br>assembled system elements. [Adapted from INCOSE<br>SE Handbook 2015]|<br> <br> <br>product|TEC.8|
|Integration approach|Describes the approach for integration or assembly of<br>system elements (e.g. software), including provision<br>of facilities, tools and resources and preparation for<br>integration testing. It defines the scheme of actions,<br>timing and resources governing the build, buy, or reuse<br>actions that make available a system element (e.g.<br>software) ready for system assembly. [Adapted from<br>ISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br> <br> <br>plan|TEC.8|



**61** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Integration record|Presents the results from the integration of the system/<br>software, which may include software components or<br>software combined with the hardware configuration<br>items and manual operations. [Adapted from ISO/IEC/<br>IEEE 15289]|<br> <br>record|TEC.8|
|Integration report|Presents the results from the integration of the system,<br>which may include software components or software<br>combined with the hardware configuration items and<br>manual operations.[Adapted from ISO/IEC/IEEE 15289]|<br> <br> <br>report|TEC.8|
|Knowledge asset|Any permanent, readable form of data, information,<br>or knowledge that can be captured in the knowledge<br>management system.|<br> <br>record|ORG.6|
|Knowledge manage‑<br>ment report|An account prepared for interested parties in order<br>to communicate the status, results, and outcomes of<br>the knowledge management activities. [INCOSE SE<br>Handbook 2015]|<br> <br> <br>report|ORG.6|
|Knowledge manage‑<br>ment strategy|Establishes how the organization and projects within<br>the organization will interact to ensure the right level<br>of knowledge is captured to provide useful knowledge<br>assets.[INCOSE SE Handbook 2015]|<br> <br> <br>plan|ORG.6|
|Knowledge manage‑<br>ment system|System used to support and enable knowledge man‑<br>agement.|product|ORG.6|
|Life cycle concepts|Articulation and refinement of the various life cycle<br>concepts consistent with the business needs in the<br>form of life cycle concept documents on which the<br>system of interest /software is based, assessed, and<br>selected. The architecture is based on these concepts,<br>and they are essential in providing context for proper<br>interpretation of the system/software requirements.<br>Typical concepts include: Acquisition concept; Deploy‑<br>ment concept; Operational concept (OpsCon); Support<br>concept; Retirement concept. [Adapted from INCOSE<br>SE Handbook 2015]|<br> <br> <br> <br> <br> <br> <br> <br> <br>description|TEC.1, TEC.2|
|Life cycle model man‑<br>agement record|Permanent, readable form of data, information, or<br>knowledge related to life cycle model management.<br>[INCOSE SE Handbook 2015]|<br> <br>record|ORG.1|
|Life cycle model man‑<br>agement report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>life cycle model management activities. [INCOSE SE<br>Handbook 2015]|<br> <br> <br>report|ORG.1|
|Life cycle model man‑<br>agement strategy|Approaches, schedules, resources, and specific consid‑<br>erations required to define a set of organizational life<br>cycle models. Includes identification of new needs and<br>the evaluation of competitiveness from the perspec‑<br>tive of the organization strategy. Includes criteria for<br>assessments and approvals/ disapprovals. [INCOSE SE<br>Handbook 2015]|<br> <br> <br> <br>plan|ORG.1|
|Life cycle models|Framework of processes and activities concerned with<br>the life cycle that can be organized into stages, which<br>also acts as a common reference for communication<br>and understanding.[ISO/IEC/IEEE 15288]|<br> <br> <br>description|ORG.1|
|Maintained system/<br>software|System/software that has been maintained for use in<br>its operational environment.|<br>product|TEC.13|
|Maintenance approach|Presents how the organization or project plans to meet<br>systems/software availability requirements and conduct<br>maintenance (logistics) activities. [Adapted from ISO/<br>IEC/IEEE 15289]|<br> <br>plan|TEC.13|



**62** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Maintenance record|Permanent, readable form of data, information, or<br>knowledge related to maintenance. [INCOSE SE Hand‑<br>book 2015]|<br>record|TEC.13|
|Maintenance report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>maintenance activities.[INCOSE SE Handbook 2015]|<br> <br>report|TEC.13|
|Measurement ap‑<br>proach|Identifies the needs and requirements for measurement<br>in an organization, project, or service. It identifies the<br>selected measures and the data collection, storage,<br>analysis, and reporting procedures. It defines how the<br>process and the measurements are evaluated. [Adapted<br>fromISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br>plan|MAN.7|
|Measurement record|Permanent, readable form of data, information, or<br>knowledge related to measurement. [INCOSE SE Hand‑<br>book 2015]|<br>record|MAN.7|
|Measurement register|A repository that supports the availability for use and<br>communication of all relevant measures in a timely,<br>complete, valid, and, if required, confidential manner.<br>[Adapted from INCOSE SE Handbook 2015]|<br> <br> <br>registry|MAN.7|
|Measurement report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>measurement activities.[INCOSE SE Handbook 2015]|<br> <br>report|MAN.7|
|Operation approach|Approaches, schedules, resources, and specific consider‑<br>ations required to perform system/software operations.<br>[Adapted from INCOSE SE Handbook 2015]|<br>plan|TEC.12|
|Operation record|Permanent, readable form of data, information, or knowl‑<br>edge related to operation.[INCOSE SE Handbook 2015]|record|TEC.12|
|Operation report|An account prepared for interested parties in order<br>to communicate the status, results, and outcomes of<br>the operation activities.[INCOSE SE Handbook 2015]|<br> <br>report|TEC.12|
|Operational system/<br>software|System/software being used in its operational envi‑<br>ronment.|product|TEC.12|
|Organization infra‑<br>structure|Resources and services that support the organization.<br>Organizational‑level facilities, personnel, and resources<br>for hardware fabrication, software development, system<br>implementation and integration, verification, validation,<br>etc.[INCOSE SE Handbook 2015]|<br> <br> <br> <br>description|ORG.2|
|Organization lessons<br>learned|<br>Organizational‑related lessons learned. Results from an<br>evaluation or observation of an implemented corrective<br>action that contributed to improved performance or<br>increased capability. A lesson learned also results from<br>an evaluation or observation of a positive finding that<br>did not necessarily require corrective action other than<br>sustainment.[INCOSE SE Handbook 2015]|<br> <br> <br> <br> <br> <br>record|ORG.3|
|Organization policy|Includes high‑level policy guidance to select, tailor, and<br>implement a life-cycle model in a project. It defines roles,<br>responsibility, accountability, and authority for lifecycle<br>process management, including process improvement. It<br>identifies the criteria for entering and completing each<br>life-cycle stage. It identifies and describes the organi‑<br>zation's processes to be applied in projects. [Adapted<br>fromISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br> <br>policy|ORG.1|
|Organization proce‑<br>dure|Includes specific steps to select, tailor, and implement<br>a life‑cycle model in a project. [Adapted from ISO/IEC/<br>IEEE 15289]|<br>procedure|ORG.1|



**63** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Organizational meas‑<br>urement needs|Identification of information needs of the decision<br>makers with respect to organizational expectations.<br>[Adapted from INCOSE SE Handbook 2015]|<br> <br>specification|ORG.1|
|Organizational per‑<br>formance data|Data provided for the identified organizational measure‑<br>ment needs.[Adapted from INCOSE SE Handbook 2015]|data|ORG.1|
|Portfolio management<br>record|Permanent, readable form of data, information, or<br>knowledge related to portfolio management. [INCOSE<br>SE Handbook 2015]|<br> <br>record|ORG.3|
|Portfolio management<br>report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>portfolio management activities. [INCOSE SE Handbook<br>2015]|<br> <br> <br>report|ORG.3|
|Portfolio management<br>strategy|Approaches, schedules, resources, and specific consid‑<br>erations required to define a project portfolio. [INCOSE<br>SE Handbook 2015]|<br>plan|ORG.3|
|Problem or opportu‑<br>nity statement|Used to obtain consensus among an acquirer, developer,<br>and support and user organizations on the demand for<br>a proposed system/software. [Adapted from ISO/IEC/<br>IEEE 15289]|<br> <br>description|TEC.1|
|Project assessment<br>and control approach|Approaches, schedules, resources, and specific consid‑<br>erations required to perform assessment and control<br>for aproject.[INCOSE SE Handbook 2015]|<br>plan|MAN.2|
|Project assessment<br>and control record|Permanent, readable form of data, information, or<br>knowledge related to project assessment and control.<br>[INCOSE SE Handbook 2015]|<br> <br>record|MAN.2|
|Project authorization|Authorization from the organization to initiate aproject.|record|ORG.3|
|Project authorization<br>toproceed request|Project request to the organization to proceed per the<br>agreed‑toprojectplan.|<br>request|MAN.2|
|Project budget|A prediction of the costs associated with a particular<br>project. Includes labour, infrastructure, acquisition,<br>and enabling system costs along with reserves for risk<br>management.[INCOSE SE Handbook 2015]|<br> <br> <br>record|MAN.1|
|Project change request|Requests to update any formal baselines that have been<br>established. In many cases, the need for change requests<br>is identified during the project assessment and control<br>process.[INCOSE SE Handbook 2015]|<br> <br> <br>request|MAN.2|
|Project constraints|Any constraints on the system/software arising from<br>the technical management strategy including cost,<br>schedule, and technical constraints. [Adapted from<br>INCOSE SE Handbook 2015]|<br> <br> <br>specification|MAN.1|
|Project control request|Internal project directives based on action required<br>due to deviations from the project plan. New directions<br>are communicated to both project team and customer,<br>when appropriate. If assessments are associated with a<br>decision gate, a decision to proceed, or not to proceed,<br>is taken.[INCOSE SE Handbook 2015]|<br> <br> <br> <br> <br>request|MAN.2|
|Project direction|Organizational direction to the project. Includes sus‑<br>tainment of projects meeting assessment criteria and<br>redirection or termination of projects not meeting<br>assessment criteria.[INCOSE SE Handbook 2015]|<br> <br>record|ORG.3|
|Project human re‑<br>sources needs|Arises from project planning and is directed to man‑<br>agement who can commit the human resources and, if<br>necessary, approve modifying the contract. [Adapted<br>fromISO/IEC/IEEE 15289]|<br> <br>specification|MAN.1|



**64** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Project infrastructure<br>needs|Arises from project planning and is directed to manage‑<br>ment who can commit the infrastructure resources and,<br>if necessary, approve modifying the contract. [Adapted<br>fromISO/IEC/IEEE 15289]|<br> <br>specification|MAN.1|
|P r oje c t le s son s<br>learned|Project‑related lessons learned. Results from an eval‑<br>uation or observation of an implemented corrective<br>action that contributed to improved performance or<br>increased capability. A lesson learned also results from<br>an evaluation or observation of a positive finding that<br>did not necessarily require corrective action other than<br>sustainment.[INCOSE SE Handbook 2015]|<br> <br> <br> <br> <br>record|MAN.2|
|Project measurement<br>needs|Identification of information needs of the decision<br>makers with respect to project expectations. [Adapted<br>from INCOSE SE Handbook 2015]|<br> <br>specification|MAN.2|
|Project objectives|The objectives orgoals for theproject.|description|MAN.1|
|Project performance<br>data|Data provided for the identified project measurement<br>needs.[Adapted from INCOSE SE Handbook 2015]|<br>data|MAN.2|
|Project plan (e.g. Soft‑<br>ware Development<br>Plan)|Describes the technical approach to be followed for a<br>software development effort. [ISO/IEC/IEEE 24748‑5]|<br>plan|MAN.1|
|Project planning re‑<br>cord|Permanent, readable form of data, information, or<br>knowledge related to project planning. [INCOSE SE<br>Handbook 2015]|<br> <br>record|MAN.1|
|Project portfolio|Collection of projects that addresses the strategic<br>objectives of the organization.[ISO/IEC/IEEE 12207]|<br>description|ORG.3|
|Project review result|Review artefacts that are expected through conduct of<br>the technical review and that can be considered elements<br>of exit criteria.[Adapted from IEEE 15288.2‑2014]|<br> <br>record|MAN.2|
|Project schedule|A linked list of a project’s milestones, activities, and<br>deliverables with intended start and finish dates. May<br>include a top‑level milestone schedule and multiple levels<br>(also called tiers) of schedules of increasing detail and<br>task descriptions with completion criteria and work<br>authorizations.[INCOSE SE Handbook 2015]|<br> <br> <br> <br> <br>description|MAN.1|
|Project status report|Provides results of monitoring the execution of the<br>defined plan or processes for internal or external distri‑<br>bution. It includes a summary of decisions, monitoring<br>results, action items, process or performance data, and<br>recorded process improvements. It assesses the degree<br>of adherence to the plans. It provides information about<br>projected cost, performance, and schedule risks; any<br>changes to previously approved plans and the related<br>impact to the project or organization; corrective ac‑<br>tions; risk treatment actions; and problem tracking and<br>problem analysis.[Adapted from ISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br> <br> <br> <br>report|MAN.2|
|Qualified personnel|Individual expected to perform duties on behalf of<br>the organization, including officers, employees, and<br>contractors.[ISO/IEC/IEEE 24765]|<br> <br>record|ORG.4|
|Quality assurance ap‑<br>proach|Presents the approach to fulfil the quality objectives<br>of the program, project, product or service. [Adapted<br>fromISO/IEC/IEEE 15289]|<br> <br>plan|MAN.8|
|Quality assurance cor‑<br>rective action|Action to eliminate the cause or reduce the likelihood of<br>recurrence of a detected project nonconformity or other<br>undesirable situation.[Adapted from ISO/IEC 19770‑1]|<br> <br>record|MAN.8|



**65** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Quality assurance cri‑<br>teria and methods|Rules on which a judgment or decision can be based,<br>or by which a product, service, result, or process can<br>be evaluated.[ISO/IEC/IEEE 15289]|specification|MAN.8|
|Quality assurance<br>evaluation report|Provides results of quality assurance evaluations. It<br>includes evaluation criteria. [Adapted fromISO/IEC/<br>IEEE 15289]|report|MAN.8|
|Quality assurance<br>record|Permanent, readable form of data, information, or<br>knowledge related to quality assurance. [INCOSE SE<br>Handbook 2015]|record|MAN.8|
|Quality assurance<br>report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>qualityassurance activities.[INCOSE SE Handbook 2015]|report|MAN.8|
|Quality assurance<br>system|System used to support and enable quality assurance.|product|MAN.8|
|Quality management<br>corrective action|Action to eliminate the cause or reduce the likelihood<br>of recurrence of a detected organizational noncon‑<br>formity or other undesirable situation. [Adapted from<br>ISO/IEC 19770‑1]|record|ORG.5|
|Quality management<br>criteria and methods|Rules on which a judgment or decision can be based,<br>or by which an organization can be evaluated. [ISO/<br>IEC/IEEE 15289]|specification|ORG.5|
|Quality management<br>evaluation report|Provides results of quality management evaluations. It<br>includes evaluation criteria. [Adapted fromISO/IEC/<br>IEEE 15289]|report|ORG.5|
|Quality management<br>record|Permanent, readable form of data, information, or<br>knowledge related to quality management. [INCOSE<br>SE Handbook 2015]|record|ORG.5|
|Quality management<br>report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>quality management activities. [INCOSE SE Handbook<br>2015]|report|ORG.5|
|Quality management<br>strategy|Presents the approach to fulfil the quality objectives of<br>the organization.[Adapted from ISO/IEC/IEEE 15289]|plan|ORG.5|
|Quality management<br>system|System used to support and enable quality management.|product|ORG.5|
|Request for supply|The acquirer’s request for information and commitments<br>needed from the supplier that are required to be included<br>in the potential supplier’s response. It announces the<br>acquirer's intention to potential bidders to acquire a<br>specified system, software product or service. [Adapted<br>fromISO/IEC/IEEE 15289]|request|AGR.1|
|Request for supply<br>response|Prepared by a potential supplier to support the offer of<br>a contract bid, including cost, schedule, risk statements,<br>methodology to satisfy the request for supply, experi‑<br>ences and capabilities, any recommendations to tailor<br>the request for supply or contract, and the signature of<br>the supplier’s approving authority. Informally, may be<br>prepared within an organization. [Adapted fromISO/<br>IEC/IEEE 15289]|description|AGR.2|
|Requirements im‑<br>posed on enabling<br>systems|Requirements for enabling systems of the system‑of‑in‑<br>terest (including software as a system) and organization,<br>including resources and tools. [Adapted from ISO/IEC/<br>IEEE 15289]|specification|TEC.1, TEC.2, TEC.3,<br>TEC.4, TEC.5, TEC.6,<br>TEC.7, TEC.8, TEC.9,<br>TEC .10, TEC .11,<br>TEC.12, TEC.13,<br>TEC.14|



**66** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Risk management ap‑<br>proach|Presents the conditions under which risk management<br>is performed and the context of risk management, such<br>as management and technical objectives, assumptions,<br>and constraints. It defines the approach to the identifica‑<br>tion, assessment, treatment, and monitoring of risks, as<br>well as the approach for registering risks, creating and<br>maintaining risk profiles (records), and reporting risk<br>status. It establishes risk categories and risk assessment<br>criteria. It identifies the risks to service continuity and<br>availability.[Adapted fromISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br> <br> <br> <br>plan|MAN.4|
|Risk management re‑<br>cord|Permanent, readable form of data, information, or<br>knowledge related to risk management. [INCOSE SE<br>Handbook 2015]|<br> <br>record|MAN.4|
|Risk management re‑<br>port|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>risk management activities.[INCOSE SE Handbook 2015]|<br> <br>report|MAN.4|
|Risk register|A repository that supports the availability for use and<br>communication of all relevant risk information in a<br>timely, complete, valid, and, if required, confidential<br>manner.[Adapted from INCOSE SE Handbook 2015]|<br> <br> <br>registry|MAN.4|
|Stakeholder identifi‑<br>cation|List of legitimate external and internal stakeholders with<br>an interest in the solution.[INCOSE SE Handbook 2015]|<br>description|TEC.2|
|Stakeholder needs and<br>requirements defini‑<br>tion approach|Approaches, schedules, resources, and specific consid‑<br>erations required to reflect consensus among the stake‑<br>holder classes to establish a common set of acceptable<br>requirements. Includes the approach to capture the<br>stakeholder needs, transform them into stakeholder<br>requirements, and manage them through the life cycle.<br>[INCOSE SE Handbook 2015]|<br> <br> <br> <br>plan|TEC.2|
|Stakeholder needs and<br>requirements defini‑<br>tion record|Permanent, readable form of data, information, or<br>knowledge related to stakeholder needs and require‑<br>ments definition.[INCOSE SE Handbook 2015]|<br>record|TEC.2|
|Stakeholder require‑<br>ments|Define a system/software or service that can meet the<br>needs of users and other identified stakeholders in a<br>defined environment, including their needs, wants,<br>desires, expectations, and their essential constraints,<br>such as the consequences of existing agreements, man‑<br>agement decisions and technical decisions. [Adapted<br>fromISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br>specification|TEC.2|
|Supplied system/<br>system element (e.g.<br>software)|The system or system element (product or service) is<br>delivered from the supplier to the acquirer consistent<br>with the delivery conditions of the supply agreement.<br>[INCOSE SE Handbook 2015]|<br> <br> <br>product|AGR.2|
|Supply agreement|The formal agreement between a supplier and an ac‑<br>quirer. Informally, commitments or agreements may<br>be specified between a supplier and an acquirer of the<br>same organization (sometimes called a memorandum<br>of understanding).[Adapted from ISO/IEC/IEEE 15289]|<br> <br> <br>agreement|AGR.2|
|Supply agreement<br>change request|Requests from a supplier to change an agreement with<br>an acquirer.|<br>request|AGR.2|
|Supply approach|Approaches, schedules, resources, and specific con‑<br>siderations required to identify candidate projects for<br>management consideration. May also include inputs<br>to determine supply constraints. Should also include<br>the identification of potential acquirers. [INCOSE SE<br>Handbook 2015]|<br> <br> <br> <br>plan|AGR.2|



**67** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Supply record|Permanent, readable form of data, information, or knowl‑<br>edge related to supply.[INCOSE SE Handbook 2015]|record|AGR.2|
|Supply report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>supplyactivities.[INCOSE SE Handbook 2015]|<br> <br>report|AGR.2|
|System analysis ap‑<br>proach|Approaches, schedules, resources, and specific consider‑<br>ations required to accomplish the various analyses to be<br>carried out, including methods, procedures, evaluation<br>criteria, orparameters.[INCOSE SE Handbook 2015]|<br> <br>plan|TEC.6|
|System analysis re‑<br>cord|Permanent, readable form of data, information, or<br>knowledge related to system analysis. [INCOSE SE<br>Handbook 2015]|<br> <br>record|TEC.6|
|System analysis report|An account prepared for interested parties in order to<br>communicate the status, results, and outcomes of the<br>system analysis activities.[INCOSE SE Handbook 2015]|<br> <br>report|TEC.6|
|System/software ar‑<br>chitecture assessment<br>report|Provides results of architecture assessments.|report|TEC.4|
|System/software ar‑<br>chitecture model|Includes the following: a) the fundamental conception<br>of a system‑of‑interest (including software as a system)<br>in terms of its purpose, system/software qualities (such<br>as feasibility, performance, safety and interoperabili‑<br>ty), constraints, and design decisions and rationale; b)<br>identification of the architecture's stakeholders and<br>the stakeholders' architecture‑related concerns. Key<br>stakeholders include the client, acquirers, certifiers,<br>vendors, maintainers and operators; c) definitions of<br>viewpoints to document the procedures for creating,<br>interpreting, analysing and evaluating architectural<br>data; and d) one or more views of the system/software.<br>Each architectural view is a representation of the com‑<br>plete system/software from the perspective of one or<br>more system/software concerns, for its stakeholders.<br>[Adapted fromISO/IEC/IEEE 15289]|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>description|TEC.4|
|System/software ar‑<br>chitecture rationale|Rationale for architecture selection, technological/tech‑<br>nical system element selection, and allocation between<br>system requirements and architectural entities (e.g.<br>functions, input/output flows, system elements, physical<br>interfaces, architectural characteristics, information/<br>data elements, containers, nodes, links, communication<br>resources).[INCOSE SE Handbook 2015]|<br> <br> <br> <br>description|TEC.4|
|System/software de‑<br>sign assessment re‑<br>port|Provides results of design assessments.|report|TEC.5|
|System/software de‑<br>sign model|Representation of a real‑world process, device, or con‑<br>cept.[ISO/IEC/IEEE 24765]|description|TEC.5|
|System/software de‑<br>sign rationale|Rationale for design selection, system element selection,<br>and allocation between system/software requirements<br>and system element. Includes rationale of major selected<br>implementation options and enablers. [Adapted from<br>INCOSE SE Handbook 2015]|<br> <br> <br> <br>description|TEC.5|
|System element (e.g.<br>software)|Member of a set of elements that constitutes a system<br>(e.g. software).[Adapted from ISO/IEC/IEEE 24748‑1]|<br>product|TEC.7|



**68** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|System element (e.g.<br>software) description|Applies the system/software architecture description<br>to the low-level system configuration items and ele‑<br>ments (e.g. software). It is at a level of detail to permit<br>design, implementation and test. [Adapted fromISO/<br>IEC/IEEE 15289]|description|TEC.5, TEC.7|
|System function model|Definition of the functional boundaries of the system/<br>software and the functions the system/software must<br>perform.[Adapted from INCOSE SE Handbook 2015]|description|TEC.3|
|System/software in‑<br>terface definition|Description of the architecture and design of interfaces<br>between system/software and components. [Adapted<br>from ISO/IEC/IEEE 24765]|description|TEC.4, TEC.5, TEC.8|
|System/software re‑<br>quirements|Includes the following: a) technical specifications for<br>the selected system‑of interest (including software as<br>a system); b) usability specifications for the envisaged<br>human-system/software interaction; c) system/soft‑<br>ware-level functions; d) safety and security require‑<br>ments; e) critical maximum and minimum performance<br>constraints; f) references to related system/software<br>design and testing standards; and g) Traceability of<br>requirements to stakeholder needs and to system/<br>software functions or components. Each requirement<br>should be uniquely identified. [Adapted from ISO/IEC/<br>IEEE 15289]|specification|TEC.3|
|System/software re‑<br>quirements definition<br>approach|Approaches, techniques, resources, and specific con‑<br>siderations required to be used to identify and define<br>the system/software requirements and manage the<br>requirements through the life cycle. [Adapted from<br>INCOSE SE Handbook 2015]|plan|TEC.3|
|System/software re‑<br>quirements definition<br>record|Permanent, readable form of data, information, or<br>knowledge related to system/software requirements<br>definition.[Adapted from INCOSE SE Handbook 2015]|record|TEC.3|
|Traceability mapping|Discernible association among two or more logical<br>entities, such as requirements, system elements, veri‑<br>fications, or tasks. [ISO/IEC TR 29110-1]|record|TEC.1, TEC.2, TEC.3,<br>TEC.4, TEC.5, TEC.6,<br>TEC.7, TEC.8, TEC.9,<br>TEC .10, TEC .11,<br>TEC.12, TEC.13,<br>TEC.14|
|Trained maintainer|Trained individual or organization that performs the<br>maintenance of a system/software. [Adapted from ISO/<br>IEC/IEEE 24748‑1]|record|TEC.13|
|Trained operator|Trained individual or organization that performs the<br>operations of a system/software. [Adapted from ISO/<br>IEC/IEEE 24748‑1]|record|TEC.12|
|Transition approach|Provides the approach for transitioning a system/<br>software into its target environment. [Adapted from<br>ISO/IEC/IEEE 15289]|plan|TEC.10|
|Transition record|Permanent, readable form of data, information, or knowl‑<br>edge related to transition.[INCOSE SE Handbook 2015]|record|TEC.10|
|Transition report|An account prepared for interested parties in order<br>to communicate the status, results, and outcomes of<br>the transition activities.[INCOSE SE Handbook 2015]|report|TEC.10|
|Validated system/<br>software|Validated system (or system element) ready for supply<br>and operation.[Adapted from INCOSE SE Handbook 2015]|product|TEC.11|



**69** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



|**Process output**|**Process output description**|**Category**|**Output of**|
|---|---|---|---|
|Validation approach|Presents the validation strategy: how the validation<br>process is to be conducted, including items subject to<br>validation; validation criteria, validation tasks; resources,<br>responsibilities, tools, and schedule; and procedures<br>for recording and reporting results of validation. It<br>identifies the methods used for validation; the prod‑<br>ucts, interfaces, and the processes that produced the<br>products. It specifies the organizational relationships<br>and degrees of independence between development<br>activities and validation activities. [Adapted from ISO/<br>IEC/IEEE 15289]|<br> <br>plan|TEC.11|
|Validation criteria|The validation criteria (the measures to be assessed),<br>who will perform validation activities, and the valida‑<br>tion environments of the system of interest (including<br>software as a system). [Adapted from INCOSE SE<br>Handbook 2015]|<br> <br>specification|TEC.1, TEC.2, TEC.11|
|Validation record|Permanent, readable form of data, information, or knowl‑<br>edge related to validation.[INCOSE SE Handbook 2015]|record|TEC.11|
|Validation report|Provides the results and conclusions of validation on<br>a system or system element. It enables the acquirer to<br>assess the validation and its results. It includes system<br>identification and overview, validation requirements<br>and criteria, overview of results, identification of items<br>validated and dates of validation, detailed results,<br>problems encountered, and rationale for decisions.<br>[Adapted fromISO/IEC/IEEE 15289]|<br> <br> <br>report|TEC.11|
|Verification approach|Presents the verification strategy: how the verification<br>process is to be conducted, including items subject<br>to verification criteria, verification tasks; resources,<br>responsibilities, tools, and schedule; and procedures<br>for recording and reporting results of verification. It<br>identifies the methods used for verification; the prod‑<br>ucts, interfaces, and the processes that produced the<br>products. It specifies the organizational relationships<br>and degrees of independence between development<br>activities and verification activities. [Adapted from<br>ISO/IEC/IEEE 15289]|<br> <br> <br> <br>plan|TEC.3, TEC.9|
|Verification criteria|The verification criteria (the measures to be assessed),<br>who will perform verification activities, and the verifi‑<br>cation environments of the system of interest. [INCOSE<br>SE Handbook 2015]|specification||
|Verification record|Permanent, readable form of data, information, or knowl‑<br>edge related to verification.[INCOSE SE Handbook 2015]|record|TEC.9|
|Verification report|Provides the results and conclusions of verification on<br>a system or system element. It enables the acquirer to<br>assess the verification and its results. It includes system<br>identification and overview, verification requirements<br>and criteria, overview of results, identification of items<br>verified and dates of verification, detailed results, prob‑<br>lems encountered, and rationale for decisions. [Adapted<br>fromISO/IEC/IEEE 15289]|report|TEC.9|
|Verified system/soft‑<br>ware|Verified system (or system element) ready for transition.<br>[INCOSE SE Handbook 2015]|product|TEC.9|
|Work Breakdown<br>Structure|<br>Deliverable‑oriented hierarchical decomposition of the<br>work to be executed by the project team to accomplish<br>the project objectives and create the required deliver‑<br>ables.[ISO/IEC TR 29110‑5‑6‑2]|description|MAN.1|



**70** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



#### **A.2 Process output categories** 

<u>Table A.2</u> describes the categories of process outputs. The category description characterizes the distinctive nature or features of the category. 

**Table A.2 — Process output categories** 

|**Category**|**Category description**|
|---|---|
|agreement|Mutual acknowledgement of terms and conditions under which a working relationship is<br>conducted.[ISO/IEC/IEEE 15288]|
|data|Representation of facts, concepts, or instructions in a manner suitable for communication,<br>interpretation, orprocessingbyhumans or byautomatic means.[ISO/IEC/IEEE 24765]|
|description|Planned or actual concept, function, design, or object.[ISO/IEC/IEEE 15289]|
|plan|Systematic course of action for achieving a declared purpose, including when, how, and by<br>whom specific activities are to beperformed.[ISO/IEC/IEEE 15289]|
|policy|Clear and measurable statements of preferred direction and behaviour to condition the<br>decisions made within an organization.[ISO/IEC/IEEE 15289]|
|procedure|An ordered series of steps toperform aprocess, activity, or task.[ISO/IEC/IEEE 15289]|
|product|Result of a process. [ISO/IEC/IEEE 15288]<br>NOTE: Includes systems that are both products and services, and systems elements such<br>as software and hardwareproducts|
|record|Set of related data items treated as a unit to state results achieved or to provide evidence<br>of activitiesperformed.[ISO/IEC/IEEE 15289 andISO 9000]|
|registry|Book or system for keeping an official list or record of work products and the associated<br>information items. [ISO/IEC/IEEE 24765]<br>Note: Repository and library items can be recorded in registries to enable better manage‑<br>ment andgovernance of these items|
|report|Results of activities such as investigations, assessments, and tests. A report communicates<br>decisions.[ISO/IEC/IEEE 15289]|
|request|Defined course of action or change to fulfil a need.[ISO/IEC/IEEE 15289]|
|specification|Identifies, in a complete, precise, and verifiable manner, the requirements, design, behaviour,<br>or other expected characteristics of a system, service, orprocess.[ISO/IEC/IEEE 15289]|



**71** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



### **Bibliography** 

- [1] ISO Guide 73:2009, _Risk management — Vocabulary_ 

- [2] ISO 9000:2015, _Quality management systems — Fundamentals and vocabulary_ 

- [3] <u>ISO 9001,</u> _Quality management systems — Requirements_ 

- [4] ISO/IEC/IEEE 14764, _Software Engineering — Software Life Cycle Processes — Maintenance_ 

- [5] <u>ISO/IEC/IEEE 15288:2015,</u> _Systems and software engineering — System life cycle processes_ 

- [6] <u>ISO/IEC/IEEE 15289,</u> _Systems and software engineering — Content of life-cycle information items (documentation)_ 

- [7] <u>ISO/IEC 16350,</u> _Information technology — Systems and software engineering — Application management_ 

- [8] ISO/IEC TR 19759:2015, _Software Engineering — Guide to the software engineering body of knowledge (SWEBOK)_ 

- [9] <u>ISO/IEC 19770‑1,</u> _Information technology — IT asset management — Part 1: IT asset management systems — Requirements_ 

- [10] <u>ISO/IEC 20000‑1,</u> _Information technology — Service management — Part 1: Service management system requirements_ 

- [11] ISO/IEC/IEEE 24748‑1, _Systems and software engineering — Life cycle management — Part 1: Guidelines for life cycle management_ 

- [12] ISO/IEC/IEEE 24748‑5, _Systems and software engineering — Life cycle management — Part 5: Software development planning_ 

- [13] ISO/IEC/IEEE 24765, _Systems and software engineering — Vocabulary_ 

- [14] <u>ISO/IEC 26550,</u> _Software and systems engineering — Reference model for product line engineering and management_ 

- [15] ISO/IEC 27002, _Information technology — Security techniques —Code of practice for information security controls_ 

- [16] ISO/IEC 27034, _Information technology — Application security_ 

- [17] ISO/IEC 27036, _Information technology — Security techniques — Information security for supplier relationships_ 

- [18] ISO/IEC TR 29110‑1, _Systems and software engineering — Lifecycle profiles for Very Small Entities (VSEs) — Part 1: Overview_ 

- [19] ISO/IEC TR 29110‑5‑6‑2, _Systems and software engineering — Lifecycle profiles for Very Small Entities (VSEs) — Part 5-6-2: Systems engineering — Management and engineering guide: Generic profile group: Basic profile_ 

- [20] ISO/IEC/IEEE 29119, _Software and systems engineering — Software testing_ 

- [21] <u>ISO/IEC/IEEE 29148,</u> _Systems and software engineering — Life cycle processes — Requirements engineering_ 

- [22] <u>ISO/IEC 33002:2015,</u> _Information technology — Process assessment — Requirements for performing process assessment_ 

**72** 

© ISO 2021 – All rights reserved 

PD ISO/IEC TS 33061:2021 **ISO/IEC TS 33061:2021** 



- [23] ISO/IEC 33020:2019, _Information technology — Process assessment — Process measurement framework for assessment of process capability_ 

- [24] <u>ISO/IEC/IEEE 42010,</u> _Systems and software engineering — Architecture description_ 

- [25] IEEE 730‑2014, _IEEE Standard for Software Quality Assurance Processes_ 

- [26] IEEE 1012‑2012, _IEEE Standard for System and Software Verification and Validation_ 

- [27] IEEE 15288.2‑2014, _IEEE Standard for Technical Reviews and Audits on Defense Programs_ 

- [28] INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities, Fourth Edition. ©  2015 John Wiley & Sons, Inc. Published 2015 by John Wiley & Sons, Inc. 

**73** 

© ISO 2021 – All rights reserved 

NO COPYING WITHOUT BSI PERMISSION EXCEPT AS PERMITTED BY COPYRIGHT LAW 



# British Standards Institution (BSI) 

BSI is the national body responsible for preparing British Standards and other standards-related publications, information and services. 

BSI is incorporated by Royal Charter. British Standards and other standardization products are published by BSI Standards Limited. 

###### **About us** 

###### **Reproducing extracts** 

For permission to reproduce content from BSI publications contact the BSI Copyright and Licensing team. 

We bring together business, industry, government, consumers, innovators and others to shape their combined experience and expertise into standards -based solutions. 

###### **Subscriptions** 

The knowledge embodied in our standards has been carefully assembled in a dependable format and refined through our open consultation process. Organizations of all sizes and across all sectors choose standards to help them achieve their goals. 

Our range of subscription services are designed to make using standards easier for you. For further information on our subscription products go to bsigroup. com/subscriptions. 

With **British Standards Online (BSOL)** you’ll have instant access to over 55,000 British and adopted European and international standards from your desktop. It’s available 24/7 and is refreshed daily so you’ll always be up to date. You can keep in touch with standards developments and receive substantial discounts on the purchase price of standards, both in single copy and subscription format, by becoming a **BSI Subscribing Member.** 

###### **Information on standards** 

We can provide you with the knowledge that your organization needs to succeed. Find out more about British Standards by visiting our website at bsigroup.com/standards or contacting our Customer Services team or Knowledge Centre. 

**PLUS** is an updating service exclusive to BSI Subscribing Members. You will automatically receive the latest hard copy of your standards when they’re revised or replaced. 

###### **Buying standards** 

You can buy and download PDF versions of BSI publications, including British and adopted European and international standards, through our website at bsigroup. com/shop, where hard copies can also be purchased. If you need international and foreign standards from other Standards Development Organizations, hard copies can be ordered from our Customer Services team. 

To find out more about becoming a BSI Subscribing Member and the benefits of membership, please visit bsigroup.com/shop. 

With a **Multi-User Network Licence (MUNL)** you are able to host standards publications on your intranet. Licences can cover as few or as many users as you wish. With updates supplied as soon as they’re available, you can be sure your documentation is current. For further information, email cservices@bsigroup.com. 

###### **Copyright in BSI publications** 

All the content in BSI publications, including British Standards, is the property of and copyrighted by BSI or some person or entity that owns copyright in the information used (such as the international standardization bodies) and has formally licensed such information to BSI for commercial publication and use. Save for the provisions below, you may not transfer, share or disseminate any portion of the standard to any other person. You may not adapt, distribute, commercially exploit or publicly display the standard or any portion thereof in any manner whatsoever without BSI’s prior written consent. 

###### **Revisions** 

Our British Standards and other publications are updated by amendment or revision. We continually improve the quality of our products and services to benefit your business. If you find an inaccuracy or ambiguity within a British Standard or other BSI publication please inform the Knowledge Centre. 

###### **Useful Contacts** 

###### **Storing and using standards** 

**Customer Services Tel:** +44 345 086 9001 **Email:** cservices@bsigroup.com 

Standards purchased in soft copy format: 

- A British Standard purchased in soft copy format is licensed to a sole named user for personal or internal company use only. 

**Subscriptions Tel:** +44 345 086 9001 **Email:** subscriptions@bsigroup.com 

- The standard may be stored on more than one device provided that it is accessible by the sole named user only and that only one copy is accessed at any one time. 

**Knowledge Centre Tel:** +44 20 8996 7004 **Email:** knowledgecentre@bsigroup.com 

- A single paper copy may be printed for personal or internal company use only. 

Standards purchased in hard copy format: 

- A British Standard purchased in hard copy format is for personal or internal company use only. 

**Copyright & Licensing** 

**Tel:** +44 20 8996 7070 **Email:** copyright@bsigroup.com 

- It may not be further reproduced – in any format – to create an additional copy. This includes scanning of the document. 

If you need more than one copy of the document, or if you wish to share the document on an internal network, you can save money by choosing a subscription product (see ‘Subscriptions’). 

###### **BSI Group Headquarters** 

389 Chiswick High Road London W4 4AL UK 



_<mark>This page deliberately left blank</mark>_ 

