import java.util.List;
/**
 * @author Alexis Biver
 *
 * PostingList : Object to represent the posting list of a dictionary
 *
 * Global Variables :
 * docIdDecimal : List representing the DocIds under decimal form
 * docIdBinary : List representing the DocIds under binary form
 * gammaCode : List representing the calculated gammaCodes
 */
public class PostingList {

    private List<String> docIdDecimal;
    private List<String> docIdBinary;
    private List<String> gammaCode;


    /**
     * add a posting to the posting list
     * @param decimal
     */
    public void addPosting(int decimal){
        this.docIdDecimal.add(Integer.toString(decimal));
        this.docIdBinary.add(Integer.toBinaryString(decimal));
        this.gammaCode.add(calculGammaCode());
    }

    //TODO : calcul the gamma code for the given ids with the gap
    private String calculGammaCode() {
        return  "ok";
    }


    /**  Setters and getters  */
    public List<String> getDocIdDecimal() {
        return docIdDecimal;
    }

    public void setDocIdDecimal(List<String> docIdDecimal) {
        this.docIdDecimal = docIdDecimal;
    }

    public List<String> getDocIdBinary() {
        return docIdBinary;
    }

    public void setDocIdBinary(List<String> docIdBinary) {
        this.docIdBinary = docIdBinary;
    }

    public List<String> getGammaCode() {
        return gammaCode;
    }

    public void setGammaCode(List<String> gammaCode) {
        this.gammaCode = gammaCode;
    }
    /**-------------------*/
}
