Title: Abstrakte Datentypen vs Datenstrukturen
Date:   2014-09-19
Category: DataTypes
Tags: datastructures,meta,datatypes,basics
Slug: adt-de
Authors: rixx
Summary: Abstrakte Datentypen und Datenstrukturen sind zwei sehr unterschiedliche Dinge, und den Unterschied zwischen den beiden zu verstehen, ist wichtig, um die folgenden Artikel über Datentypen, Datenstrukturen und verschiedene Implementierungen zu verstehen.

**zl;ng:** ADT: Definition eines Stacks als `Daten + push + pop + peek`. Datenstruktur: Implementierung eines Stacks als `verkettete Liste + push() + pop() + peek()`.

Es gibt einen Unterschied zwischen ADT (abstrakten Datentypen, *abstract data types*) und Datenstrukturen. Wer den nicht versteht, hat möglicherweise mit den folgenden Artikeln über Datentypen und Datenstrukturen Schwierigkeiten, deshalb hier eine kurze Einführung.


## Abstrakte Datentypen
*Abstrakte Datentypen* werden durch die Operationen definiert, die auf ihnen ausgeführt werden können. Sie sind nur ein Modell von Daten und den ihnen zugeordneten Methoden. Man kann sie sich etwa wie ein Interface in Java-Terminologie vorstellen.

Ein ADT kann viele verschiedene Implementierungen haben, die sich in konkreten Punkten wie der Implementierung von Algorithmen oder der Nutzung vollkommen verschiedener Datenstrukturen unterscheiden können.

**Beispiele:** Eine Liste ist ein ADT, und wird üblicherweise über die Funktionen `insert`, `get` und `delete` definiert (möglicherweise unter etwas anderen Namen). Der Stack ist ein weiterer bekannter ADT, der durch die Operationen `push`, `pop` und manchmal `peek` beschrieben wird.

## Datendstrukturen
*Datenstrukturen* dienen dazu, Daten so zu organisieren, dass sie gut genutzt werden können. Datenstrukturen kombiniert mit den benötigten Funktionen oder Methoden können Implementierungen eines ADT darstellen. Datenstrukturen, die in vielen Programmiersprachen zur Verfügung gestellt werden, sind zum Beispiel Strings, Integers, Listen, Dictionaries und Fließkommazahlen.

**Beispiele:** Eine verkettete Liste kann eine Implementierung eines Stacks oder einer Liste sein, je nach dem, mit welchen Funktionen sie gepaart wird.


