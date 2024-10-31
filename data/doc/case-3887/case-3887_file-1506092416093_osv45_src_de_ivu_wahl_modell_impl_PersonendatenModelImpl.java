package de.ivu.wahl.modell.impl;

/**
 * PersonendatenModelImpl
 *
 * @author cos@ivu.de  (c) 2003-7 Statistisches Bundesamt und IVU Traffic Technologies AG

 */

import java.util.List;

import org.apache.log4j.Category;

import de.ivu.util.debug.Log4J;

public class PersonendatenModelImpl extends BasicPersonendatenModelImpl {
  private static final long serialVersionUID = -9019850877482508509L;
  private static final Category LOGGER = Log4J.configure(PersonendatenModelImpl.class);
  static {
    LOGGER
        .info(Log4J.dumpVersion(PersonendatenModelImpl.class, Log4J.extractVersion("$Revision$"))); //$NON-NLS-1$
  }

  /**
   * Constructor
   * 
   * @param id_Personendaten
   */
  public PersonendatenModelImpl() {
    super();
  }

  /**
   * Constructor
   * 
   * @param id_Personendaten
   */
  public PersonendatenModelImpl(String id_Personendaten) {
    super(id_Personendaten);
  }

  @Override
  public String getAnzeigeName() {
    StringBuilder name = new StringBuilder();
    if (getPraefix() != null) {
      name.append(getPraefix()).append(" "); //$NON-NLS-1$
    }
    name.append(getNachname());
    if (getInitialen() != null) {
      name.append(", ").append(getInitialen()); //$NON-NLS-1$
    }
    return name.toString();
  }

  @Override
  public boolean hasListenkandidatur() {
    throw new UnsupportedOperationException("Method not supported."); //$NON-NLS-1$
  }

  @Override
  public List<Integer> getListenkandidaturenGruppenSchluesselSortiert() {
    throw new UnsupportedOperationException("Method not supported."); //$NON-NLS-1$
  }

}