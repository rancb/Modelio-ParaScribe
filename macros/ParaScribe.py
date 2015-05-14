def indent(nb, character=' '):
    return character*nb


if len(selectedElements)==0:
    print "Vous n'avez pas d'element selectionne"

else:
    for element in selectedElements:
        if isinstance(element, Class):
            print "Le concept de %s est pertinent." % (element.name)
            print

            # Attributs
            attributes = element.ownedAttribute
            for attribute in attributes:
                print indent(4) + "Le %s de %s est un %s" % (attribute.name, element.name, attribute.type.name)
            print

            # Methodes
            methods = element.getOwnedOperation()
            if len(methods) > 0:
                print indent(4) + "Pour un %s donne il est possible de :" % (element.name)
                for method in methods:
                    string = "- %s" % (method.name)
                    parameters = method.getIO()
                    for parameter in parameters:
                        string = string + " avec un(e) %s" % (parameter.name)
                    print indent(8) + string + "."
                print

            # Associations
            # TODO : erreur lorsque l'association est une composition
            associations = element.compositionChildren
            for children in associations:
                if children.getMClass().toString() == 'AssociationEnd SmClass':
                    print indent(4) + "Un(e) %s %s un ou des %s." % (element.name, children.association.name, children.target.name)
                    print indent(4) + "Le ou les %s de %s est un ou sont tous des %s." % (children.name, element.name, children.target.name)
                    print indent(4) + "Le ou les %s de %s est un ou sont tous des %s." % (children.opposite.name, children.target.name, element.name)
                    # Cardinalite
                    maxi = children.multiplicityMax
                    mini = children.multiplicityMin
                    if mini == maxi:
                        print indent(8) + "Un(e) %s quelconque a toujours %s %s." % (element.name, mini, children.name)
                    else:
                        if mini == "0":
                            print indent(8) + "Un(e) %s quelconque peut ne pas avoir de %s." % (element.name, children.name)
                        else:
                            print indent(8) + "Un(e) %s quelconque doit avoir au moins %s %s." % (element.name, mini, children.name)
                        if maxi == "*":
                            print indent(8) + "Un(e) %s quelconque peut avoir plusieurs %s." % (element.name, children.name)
                        else:
                            print indent(8) + "Un(e) %s quelconque peut avoir au plus %s %s." % (element.name, maxi, children.name)
                    print indent(8) + "Tous les %s d'un(e) %s sont des %s." % (children.name, element.name, children.target.name)

                    maxi = children.opposite.multiplicityMax
                    mini = children.opposite.multiplicityMin
                    if mini == maxi:
                        print indent(8) + "Un(e) %s quelconque a toujours %s %s." % (children.target.name, mini, children.opposite.name)
                    else:
                        if mini == "0":
                            print indent(8) + "Un(e) %s quelconque peut ne pas avoir de %s." % (children.target.name, children.opposite.name)
                        else:
                            print indent(8) + "Un(e) %s quelconque doit avoir au moins %s %s." % (children.target.name, mini, children.opposite.name)
                        if maxi == "*":
                            print indent(8) + "Un(e) %s quelconque peut avoir plusieurs %s." % (children.target.name, children.opposite.name)
                        else:
                            print indent(8) + "Un(e) %s quelconque peut avoir au plus %s %s." % (children.target.name, maxi, children.opposite.name)
                    print indent(8) + "Tous les %s d'un(e) %s sont des %s." % (children.opposite.name, children.target.name, element.name)
                    print

            # Heritage
            parents = element.parent
            if len(parents) > 0:
                print indent(4) + "%s est :" % (element.name)
            for parent in parents:
                print indent(8) + "- un(e) %s." % (parent.superType.name)
            print
            
