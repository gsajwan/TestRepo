from com.xebialabs.xlrelease.domain import Release
from com.xebialabs.xlrelease.domain.variables import ListOfStringValueProviderConfiguration


def createVariable(type, description, label, key, releaseID):
	var=Variable()
	var.setType(type)
	var.setDescription(description)	var.setLabel(label)
	var.key = key
	var = releaseApi.createVariable(releaseID,var)
	return var

# chgStart = createVariable("xlrelease.StringVariable","The start time of the change in format - yyyy-MM-dd HH:mm:ss",'Change Start Time','changeStartTime', release.id)
# chgStart.requiresValue = True
# releaseApi.updateVariable(chgStart)

# chgEnd = createVariable("xlrelease.StringVariable","The end time of the change in format - yyyy-MM-dd HH:mm:ss",'Change End Time','changeEndTime', release.id)
# chgEnd.requiresValue = True
# releaseApi.updateVariable(chgEnd)

securityTestDate = createVariable("xlrelease.StringVariable","Please include the date of the security test",'Please include the date of the security test:','securityTestDate', release.id)
securityTestDate.requiresValue = True
releaseApi.updateVariable(securityTestDate)

securityVarianceNumbers = createVariable("xlrelease.ListStringVariable","Please list Security variance numbers",'Please list Security variance numbers:','securityVarianceNumbers', release.id)

securityComments = createVariable("xlrelease.StringVariable","Please explain why a security test was not executed",'Please explain why a security test was not executed:','securityComments', release.id)
securityComments.requiresValue = True
releaseApi.updateVariable(securityComments)

performanceTestDate = createVariable("xlrelease.StringVariable","Please include the date of the performance test",'Please include the date of the performance test:','performanceTestDate', release.id)
performanceTestDate.requiresValue = True
releaseApi.updateVariable(performanceTestDate)

performanceTestComments = createVariable("xlrelease.StringVariable","Please explain why a performance test was not executed",'Please explain why a performance test was not executed:','performanceTestComments', release.id)
performanceTestComments.requiresValue = True
releaseApi.updateVariable(performanceTestComments)

automatedTestingDate = createVariable("xlrelease.StringVariable","Please include the date of the automated test",'Please include the date of the automated test:','automatedTestingDate', release.id)
automatedTestingDate.requiresValue = True
releaseApi.updateVariable(automatedTestingDate)

automatedTestingComments = createVariable("xlrelease.StringVariable","Please explain why no automated testing was executed",'Please explain why no automated testing was executed:','automatedTestingComments', release.id)
automatedTestingComments.requiresValue = True
releaseApi.updateVariable(automatedTestingComments)

functionalTestDate = createVariable("xlrelease.StringVariable","Please include the date of the functional test",'Please include the date of the functional test:','functionalTestDate', release.id)
functionalTestDate.requiresValue = True
releaseApi.updateVariable(functionalTestDate)

functionalTestComments = createVariable("xlrelease.StringVariable","Please explain why no functional testing was executed",'Please explain why no functional testing was executed:','functionalTestComments', release.id)
functionalTestComments.requiresValue = True
releaseApi.updateVariable(functionalTestComments)


# secTestYesNo = createVariable("xlrelease.StringVariable","Has a security test been run on the code base?",'Has a security test been run on the code base?','secTestYesNo', release.id)
# secTestYesNo.requiresValue = True
# releaseApi.updateVariable(secTestYesNo)
# myList = ListOfStringValueProviderConfiguration()
# myList.id = secTestYesNo.id + '/valueProvider'
# secTestYesNo.setValueProvider(myList)
# releaseApi.updateVariable(secTestYesNo)
# secTestYesNo.valueProvider.setValues(['Yes','No'])
# releaseApi.updateVariable(secTestYesNo)

secTestVulnerabilities = createVariable("xlrelease.StringVariable","Were there vulnerabilities? If so, please provide variance numbers.",'Were there vulnerabilities? If so, please provide variance numbers.','secTestVulnerabilities', release.id)
secTestVulnerabilities.requiresValue = True
releaseApi.updateVariable(secTestVulnerabilities)
myList = ListOfStringValueProviderConfiguration()
myList.id = secTestVulnerabilities.id + '/valueProvider'
secTestVulnerabilities.setValueProvider(myList)
releaseApi.updateVariable(secTestVulnerabilities)
secTestVulnerabilities.valueProvider.setValues(['Yes','No'])
releaseApi.updateVariable(secTestVulnerabilities)

# functionTestYesNo = createVariable("xlrelease.StringVariable","Has an overall functional test been completed on the application in the QV environment?",'Has an overall functional test been completed on the application in the QV environment?','functionTestYesNo', release.id)
# functionTestYesNo.requiresValue = True
# releaseApi.updateVariable(functionTestYesNo)
# myList = ListOfStringValueProviderConfiguration()
# myList.id = functionTestYesNo.id + '/valueProvider'
# functionTestYesNo.setValueProvider(myList)
# releaseApi.updateVariable(functionTestYesNo)
# functionTestYesNo.valueProvider.setValues(['Yes','No'])
# releaseApi.updateVariable(functionTestYesNo)

# perfTestYesNo = createVariable("xlrelease.StringVariable","Has a performance test been run on the application in the QV environment?",'Has a performance test been run on the application in the QV environment?','perfTestYesNo', release.id)
# perfTestYesNo.requiresValue = True
# releaseApi.updateVariable(perfTestYesNo)
# myList = ListOfStringValueProviderConfiguration()
# myList.id = perfTestYesNo.id + '/valueProvider'
# perfTestYesNo.setValueProvider(myList)
# releaseApi.updateVariable(perfTestYesNo)
# perfTestYesNo.valueProvider.setValues(['Yes','No'])
# releaseApi.updateVariable(perfTestYesNo)

# automatedTestYesNo = createVariable("xlrelease.StringVariable","Have automated testing scripts been run on the application?",'Have automated testing scripts been run on the application?','automatedTestYesNo', release.id)
# automatedTestYesNo.requiresValue = True
# releaseApi.updateVariable(automatedTestYesNo)
# myList = ListOfStringValueProviderConfiguration()
# myList.id = automatedTestYesNo.id + '/valueProvider'
# automatedTestYesNo.setValueProvider(myList)
# releaseApi.updateVariable(automatedTestYesNo)
# automatedTestYesNo.valueProvider.setValues(['Yes','No'])
# releaseApi.updateVariable(automatedTestYesNo)
