#!\/usr\/bin\/env python
# coding: utf-8

# In[9]:


import re
class Acronyms:
    def __init__(self):
        ("")
    def normalize_acronyms(self,text):
        dict_acronyms={"ሃ\.ማ\.ሓ\.ስ\.ኩ\.ኤ\.":"ሃገራዊ ማሕበር ስንኩላን ኲናት ኤርትራ","ሃ\.ማ\.ሓ\.ስ\.ኲ\.ኤ\.":"ሃገራዊ ማሕበር ስንኩላን ኲናት ኤርትራ","ሃ\.ማ\.ሓ\.ስ\.ኲ\.ኤ":"ሃገራዊ ማሕበር ስንኩላን ኲናት ኤርትራ","ሃ\.ማ\.ሓ\.ስ\.ኩ\.ኤ":"ሃገራዊ ማሕበር ስንኩላን ኲናት ኤርትራ","ሃ\.ማ\.መ\.ተ\.ኤ\.":"ሃማመተኤ","ኢ\.ሰ\.ፓ\.ኣ\.ኮ\.":"ኢሰፓ","ኢ\.ሰ\.ፓ\.ኣ\.ኮ":"ኢሰፓ","ሃ\.ማ\.መ\.ተ\.ኤ":"ሃማመተኤ","ህ\.ሓ\.ሓ\.ኤ\.":"ህዝባዊ ሓይልታት ሓርነት ኤርትራ","ህ\.ሰ\.ሓ\.ኤ\.":"ህዝባዊ ሰራዊት ሓርነት ኤርትራ","ህ\.ግ\.ሓ\.ኤ\.":"ህዝባዊ ግንባር ሓርነት ኤርትራ","ህ\.ግ\.ደ\.ፍ\.":"ህግደፍ","ቤ\/ክርስትያን":"ቤተክርስትያን","ሃ\.ማ\.ሞ\.ስ\.":"ሃማሞስ","ሃ\.ማ\.ደ\.ኤ\.":"ሃማደኤ","ኤች\.ኣይ\.ቪ\.":"ኤችኣይቪ","ኤፍ\.ቢ\.ኣይ\.":"ኤፍቢኣይ","ሃ\.ማ\.ደ\.ኤ":"ሃማደኤ","ሕ\/ሲ\/ስ\/ኤ":"ሕጊ ሲቪላዊ ስርዓት ኤርትራ","ሕ\/ገ\/ስ\/ኤ":"ሕጊ ገበናዊ ስርዓት ኤርትራ","ሚ\/ሃ\/ባሕሪ":"ሚኒስትሪ ሃብቲ ባሕሪ","ሚ\/ምክልኻል":"ሚኒስትሪ ምክልኻል","ሚ\/ትምህርቲ":"ሚኒስትሪ ትምህርቲ","ሚ\/ዕ\/ማ\/ድ":"ሚኒስትሪ ዕዮን ማሕበራዊ ድሕነትን","ሚ\/ዕ\/ሰ\/ድ":"ሚኒስትሪ ዕዮን ሰብኣዊ ድሕነትን","ሰ\.ቀ\.ባሕሪ":"ሰሜናዊ ቀይሕ ባሕሪ","ሰ\/ቀ\/ባሕሪ":"ሰሜናዊ ቀይሕ ባሕሪ","ቤ\/ማእሰርቲ":"ቤትማእሰርቲ","ህ\.ሰ\.ሓ\.ኤ":"ህዝባዊ ሰራዊት ሓርነት ኤርትራ","ብር\/ጀነራል":"ብርጋደር ጀነራል","ሃ\.ማ\.ሞ\.ስ":"ሃማሞስ","ህ\.ግ\.ሓ\.ኤ":"ህዝባዊ ግንባር ሓርነት ኤርትራ","ኣር\.ፒ\.ጂ\.":"ኣርፒጂ","ኤች\.ኣይ\.ቪ":"ኤችኣይቪ","ህ\.ሓ\.ሓ\.ኤ":"ህዝባዊ ሓይልታት ሓርነት ኤርትራ","ኤች\.ፓይሎሪ":"ኤችፓይሎሪ","ኤፍ\.ቢ\.ኣይ":"ኤችፓይሎሪ","ህ\.ግ\.ደ\.ፍ":"ህግደፍ","ደ\.ቀ\.ባሕሪ":"ደቡባዊ ቀይሕ ባሕሪ","ደ\/ቀ\/ባሕሪ":"ደቡባዊ ቀይሕ ባሕሪ","ህ\.ሰራዊት":"ህዝባዊ ሰራዊት","መ\/መሳርዕ":"መራሒ መሳርዕ","ቁ\.ሳ\.ጶ\.":"ቊጽሪ ሳጹን ጶስታ","ቅ\.ል\.ክ\.":"ቅድሚ ልደተ ክርስቶስ","ቊ\.ሳ\.ጶ\.":"ቊጽሪ ሳጹን ጶስታ","መ\/መስርዕ":"መራሒ መስርዕ","መ\/ብርጌድ":"መራሒ ብርጌድ","ቤ\/ጽሕፈት":"ቤትጽሕፈት","ብ\/ጀነራል":"ብርጋደር ጀነራል","መ\/ቦጦሎኒ":"መራሒ ቦጦሎኒ","ተ\.ሓ\.ኤ\.":"ተጋድሎ ሓርነት ኤርትራ","ኢ\.ሰ\.ፓ\.":"ኢሰፓ","ህ\.ግንባር":"ህዝባዊ ግንባር","ሌ\/ኮሎኔል":"ሌተናል ኮሎኔል","ኣር\.ፒ\.ጂ":"ኣርፒጂ","ሚ\/ቱሪዝም":"ሚኒስትሪ ቱሪዝም","ሌ\/ኮሎኔል":"ሌተናል ኮሎኔል","ሕ\.መ\.ኣ\.":"ሕቡራት መንግስታት ኣመሪካ","ሃ\/ማርያም":"ሃይለማርያም","ማ\.ሞ\.ስ\.":"ማእከል ሞያዊ ስልጠናታት ማሞስ","ማ\.ት\.ኣ\.":"ማትኣ","ክ\/ማርያም":"ክፍለ ማርያም","ክ\/ሰራዊት":"ክፍለ ሰራዊት","ወ\.ዘ\.ተ\.":"ወዘተ","ወ\/ትንሳኤ":"ወልደትንሳኤ","ው\.ሕ\.ሃ\.":"ውድብ ሕቡራት ሃገራት","ደ\.ቀ\.ባ\.":"ደቡባዊ ቀይሕ ባሕሪ","ሜ\/ጀነራል":"ሜጀር ጀነራል","ሰ\.ቀ\.ባ\.":"ሰሜናዊ ቀይሕ ባሕሪ","ድ\.ል\.ክ\.":"ድሕሪ ልደተ ክርስቶስ","ገ\/ሚካኤል":"ገብረሚካኤል","ገ\/ማርያም":"ገብረማርያም","ማ\.ት\.ኣ":"ማሕበር ትያትር ኣስመራ","ሚ\/ሕርሻ":"ሚኒስትሪ ሕርሻ","ተ\.ሓ\.ኤ":"ተጋድሎ ሓርነት ኤርትራ","ሚ\/ሜተር":"ሚሊ ሜተር","ኢ\.ሰ\.ፓ":"ኢሰፓ","ሰ\.ቀ\.ባ":"ሰሜናዊ ቀይሕ ባሕሪ","ሚ\/ሜትር":"ሚሊ ሜተር","ሃ\/ስላሴ":"ሃይለስላሴ","ሰ\/ቀ\/ባ":"ሰሜናዊ ቀይሕ ባሕሪ","ሕ\/ሲ\/ስ":"ሕጊ ሲቪላዊ ስርዓት","ሲ\/ሕ\/ኤ":"ሲቪላዊ ሕጊ ኤርትራ","ቁ\.ሳ\.ጶ":"ቊጽሪ ሳጹን ጶስታ","ሓ\/ባሕሪ":"ሓይሊ ባሕሪ","ቁ\.ስልኪ":"ቊጽሪ ስልኪ","ቅ\.ል\.ክ":"ቅድሚ ልደተ ክርስቶስ","ኪ\/ሜተር":"ኪሎ ሜተር"                       ,"ኪ\/ሜትር":"ኪሎ ሜተር","ሕ\/ገ\/ስ":"ሕጊ ገበናዊ ስርዓት","ቅ\.ቀትሪ":"ቅድሚ ቀትሪ","ክ\/ዘመን":"ክፍለ ዘመን","ወ\.ዘ\.ተ":"ወዘተ","ቅ\.ቐትሪ":"ቅድሚ ቀትሪ","ቅ\/ቀትሪ":"ቅድሚ ቀትሪ","ው\.ሕ\.ሃ":"ውድብ ሕቡራት ሃገራት","ቅ\/ቐትሪ":"ቅድሚ ቀትሪ","ደ\.ቀ\.ባ":"ደቡባዊ ቀይሕ ባሕሪ","ቊ\.ሳ\.ጶ":"ቊጽሪ ሳጹን ጶስታ","መ\/ጋንታ":"መራሒ ጋንታ","ደ\/ቀ\/ባ":"ደቡባዊ ቀይሕ ባሕሪ","ቊ\.ስልኪ":"ቊጽሪ ስልኪ","ዲ\.ዲ\.ቲ":"ዲዲቲ","ድ\.ል\.ክ":"ድሕሪ ልደተ ክርስቶስ","ሚ\/ጥዕና":"ሚኒስትሪ ጥዕና","ድ\.ቀትሪ":"ድሕሪ ቀትሪ","ድ\.ቐትሪ":"ድሕሪ ቀትሪ","ድ\/ቀትሪ":"ድሕሪ ቀትሪ","ድ\/ቐትሪ":"ድሕሪ ቀትሪ","ገ\/ሕ\/ኤ":"ገበናዊ ሕጊ ኤርትራ","ማ\.ሞ\.ስ":"ማእከል ሞያዊ ስልጠናታት ማሞስ","ሕ\.መ\.ኣ":"ሕቡራት መንግስታት ኣመሪካ","ገ\/ኪዳን":"ገብረማርያም","ኪ\.ሎ\.":"ኪሎ","ኪ\.ሜ\.":"ኪሎ ሜተር","ኪ\.ዋ\.":"ኪሎ ዋት","ኪ\.ግ\.":"ኪሎ ግራም","ኪ\.ግ\.":"ኪሎ ግራም","ህ\.ግ\.":"ህዝባዊ ግንባር","ቤ\.ት\.":"ቤትትምህርቲ","ክ\.ሰ\.":"ክፍለ ሰራዊት","ቤ\.ክ\.":"ቤተክርስትያን","ቤ\.ጽ\.":"ቤትጽሕፈት","ሚ\.ሊ\.":"ሚሊ ሊትር","ወ\.ሮ\.":"ወይዘሮ","ሚ\/ዕዮ":"ሚኒስትሪ ዕዮ","ሲ\.ሕ\.":"ሲቪላዊ ሕጊ","ወ\/ሪት":"ወይዘሪት","ሚ\/ዜና":"ሚኒስትሪ ዜና","ወዘተ\.":"ወዘተ","ሴ\.ሜ\.":"ሰንቲ ሜተር","ሚ\.ሜ\.":"ሚሊ ሜተር","ዓ\.ም\.":"ዓመተምህረት","መ\.ም\.":"መምህር","ት\.ሜ\.":"ትርብዒት ሜተር","ን\/ዞባ":"ንኡስ ዞባ","መ\/ሓይ":"መራሒ ሓይሊ","ሕ\/ሰብ":"ሕብረተሰብ","ዲ\.ሰ\.":"ዲግሪ ሰንቲግረይድ","ዲ\.ሴ\.":"ዲግሪ ሰንቲግረይድ","ህ\.ሰ\.":"ህዝባዊ ሰራዊት","ቅ\.ቀ\.":"ቅድሚ ቀትሪ","ኢንጂ\.":"ኢንጂነር","ድ\.ቀ\.":"ድሕሪ ቀትሪ","ኢንጅ\.":"ኢንጂነር","ድ\.ቐ\.":"ድሕሪ ቀትሪ","መ\/ም\.":"መምህር","ቅ\.ቐ\.":"ቅድሚ ቀትሪ","ሰ\.ሜ\.":"ሰንቲ ሜተር","ዶ\.ር\.":"ዶክተር","ዶ\/ር\.":"ዶክተር","ገ\.ሕ\.":"ገበናዊ ሕጊ","ሰ\.ሜ\.":"ሰንቲ ሜተር","ገ\/ሄር":"ገብረእግዚኣብሄር","ሰ\.ም\.":"ሰሜናዊ ምብራቕ","ህ\.ሓ\.":"ህዝባዊ ሓይልታት","ሌ\/ኮ\/":"ሌተናል ኮሎኔል","ኪ\.ሜ":"ኪሎ ሜተር","ቅ\/ቐ":"ቅድሚ ቀትሪ","ኪ\.ዋ":"ኪሎ ዋት","ቅ\/ቐ":"ቅድሚ ቀትሪ","ኪ\.ግ":"ኪሎ ግራም","ኪ\.ግ":"ኪሎ ግራም","ህ\.ሰ":"ህዝባዊ ሰራዊት","ሚ\/ሪ":"ሚኒስትሪ","ኪ\/ሜ":"ኪሎ ሜተር","ሚ\/ር":"ሚኒስተር","ሌ\/ኮ":"ሌተናል ኮሎኔል","ክ\.ሰ":"ክፍለ ሰራዊት","ቤ\.ት":"ቤትትምህርቲ","መ\.ም":"መምህር","ክ\/ሰ":"ክፍለ ሰራዊት","ቤ\.ክ":"ቤተክርስትያን","ክ\/ዘ":"ክፍለ ዘመን","ሚ\/ዕ":"ሚኒስትሪ ዕዮ","ኮ\/ል":"ኮሎኔል","ወ\.ሮ":"ወይዘሮ","ቤ\.ጽ":"ቤትጽሕፈት","መም\.":"መምህር","ሲ\.ሕ":"ሲቪላዊ ሕጊ","ቤ\/ት":"ቤትትምህርቲ","ወ\/ሮ":"ወይዘሮ","ወ\/ት":"ወይዘሪት","ቤ\/ት":"ቤትትምህርቲ","ቤ\/ክ":"ቤተክርስትያን","መም\/":"መምህር","ቤ\/ጽ":"ቤትጽሕፈት","ዓ\.ም":"ዓመተ ምህረት","ዓ\.ም":"ዓመተ ምህረት","ሚ\.ሊ":"ሚሊ ሊትር","ዓ\/ም":"ዓመተምህረት","ብ\/ጀ":"ብርጋደር ጀነራል","ሲ\.ዲ":"ሲዲ","ሳ\.ሜ":"ሰንቲ ሜተር","ሳ\.ሜ":"ሰንቲ ሜተር","ሳ\.ሜ":"ሰንቲ ሜተር","ዲ\.ሰ":"ዲግሪ ሰንቲግረይድ","ተጋ\/":"ተጋዳላይ","ዲ\.ሴ":"ዲግሪ ሰንቲግረይድ","ዲ\.ሴ":"ዲግሪ ሰንቲግረይድ","ት\.ሜ":"ትርብዒት ሜተር","ሴ\.ሜ":"ሰንቲ ሜተር","ሌ\/ኮ":"ሌተናል ኮሎኔል","ሚ\.ሜ":"ሚሊ ሜተር","ድ\.ቀ":"ድሕሪ ቀትሪ","ድ\.ቀ":"ድሕሪ ቀትሪ","ሕ\/ሰ":"ሕብረተሰብ","ህ\.ሓ":"ህዝባዊ ሓይልታት","ድ\.ቐ":"ድሕሪ ቀትሪ","ህ\.ግ":"ህዝባዊ ግንባር","ሚ\/ሜ":"ሚሊ ሜተር","ድ\/ቀ":"ድሕሪ ቀትሪ","ድ\/ቀ":"ድሕሪ ቀትሪ","ቅ\.ቀ":"ቅድሚ ቀትሪ","ድ\/ቐ":"ድሕሪ ቀትሪ","ድ\/ቐ":"ድሕሪ ቀትሪ","ሜ\/ጀ":"ሜጀር ጀነራል","ዶ\.ር":"ዶክተር","መ\/ም":"መምህር","ዶ\/ር":"ዶክተር","ቅ\.ቐ":"ቅድሚ ቀትሪ","ዶር\.":"ዶክተር","ገ\.ሕ":"ገበናዊ ሕጊ","ምም\/":"ምምሕዳር","ሰ\.ሜ":"ሰንቲ ሜተር","ቅ\/ቀ":"ቅድሚ ቀትሪ","ቅ\/ቀ":"ቅድሚ ቀትሪ","ኪ\.ሎ":"ኪሎ","ሄ\/ር":"ሄክታር","ጉ\/ባ":"ጉጅለ ባህሊ","ጨ\/":"ጨንፈር","ሜ\.":"ሜተር","ገ\/":"ገብረ","ቁ\.":"ቁጽሪ","ቊ\.":"ቁጽሪ","ቤ\/":"ቤት","ተ\/":"ተኽለ","ክ\/":"ክፍለ","ኮ\/":"ኮሎኔል"}
        for i in dict_acronyms.keys():
            p=re.compile(i)
            text=p.sub(dict_acronyms[i],text)
        return text


# In[10]:


#(text)


# In[ ]:




